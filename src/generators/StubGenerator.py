from io import BytesIO
import re
import codecs
from typing import List, Optional, Tuple, Union
import xml.etree.ElementTree as ElementTree
from os import makedirs
from os.path import abspath, join, exists


class StubGenerator:
    script_dir: str
    version: str

    def __init__(self, script_dir: str, version: str):
        self.script_dir = script_dir
        self.version = version

    def generate(self):
        in_file = abspath(join(self.script_dir, "Live.xml"))
        out_dir = abspath(join(self.script_dir, "Live"))
        out_file = join(out_dir, "__init__.py")
        if not exists(out_dir):
            makedirs(out_dir)

        xml = self.parse_xml(in_file)
        if xml is not None:
            with codecs.open(out_file, "w", "utf-8") as f:
                f.write("# type: ignore\n")
                f.write("from types import ModuleType\n")
                f.write(f'"""Stub generated for Ableton Version  {self.version}"""\n')
                last_tag = None
                last_name = None
                last_doc = None
                for element in xml.findall("./*"):
                    if element.tag == "Doc":
                        last_doc = element.text.strip() if element.text else ""
                    else:
                        self.generate_code(last_tag, last_name, last_doc, f)
                        last_doc = None
                        last_tag = element.tag
                        last_name = element.text.strip() if element.text else ""
                self.generate_code(last_tag, last_name, last_doc, f)

    def generate_code(self, tag, name, doc, f):
        if doc is not None:
            doc = (
                doc.replace(">", ">")
                .replace("<", "<")
                .replace("&amp;gt;", ">")
                .replace("&amp;lt;", "<")
                .replace("&amp;", "&")
            )
        if tag is not None and name is not None and name != "Live":
            level = name.count(".") - 1
            indent = "    " * level
            short_name = name.split(".")[-1]
            if "(" in short_name:
                short_name = short_name.split("(")[0]

            print("Generating %s '%s'" % (tag, name))

            if tag == "Module":
                f.write("\n\n%sclass %s(ModuleType):\n" % (indent, short_name))

            if tag == "Class" or tag == "Sub-Class":
                f.write("\n%sclass %s(object):\n" % (indent, short_name))
                f.write("%s    def __init__(self, *a, **k):\n" % indent)
                indent += "    "

            if tag == "Method":
                args, ret, doc = self.parse_args_from_doc(doc)
                if args and len(args) > 0:
                    args.remove(args[0])  # remove first arg because that is "self"
                    f.write(
                        "\n%sdef %s(self, %s) -> %s:\n"
                        % (
                            indent,
                            short_name,
                            ", ".join([self.format_arg(arg) for arg in args]),
                            ret,
                        )
                    )
                    doc = "%s%s" % (doc, self.make_arg_doc(args, ret, indent + "    "))
                else:
                    f.write(
                        "\n%sdef %s(self, *a, **k) -> %s:\n" % (indent, short_name, ret)
                    )

            if tag == "Built-In":
                args, ret, doc = self.parse_args_from_doc(doc)
                f.write("\n%s@staticmethod\n" % indent)
                if args:
                    f.write(
                        "%sdef %s(%s) -> %s:\n"
                        % (
                            indent,
                            short_name,
                            ", ".join([self.format_arg(arg) for arg in args]),
                            ret,
                        )
                    )
                    doc = "%s%s" % (doc, self.make_arg_doc(args, ret, indent + "    "))
                else:
                    f.write("%sdef %s():\n" % (indent, short_name))

            if tag == "Property" or tag == "Value":
                args, ret, doc = self.parse_args_from_doc(doc)
                f.write("\n%s@property\n" % indent)
                f.write("%sdef %s(self) -> %s:\n" % (indent, short_name, ret))

            if doc:
                f.write('{0}    """\n{0}    {1}\n    {0}"""\n'.format(indent, doc))
            f.write("%s    pass\n" % indent)

    def parse_args_from_doc(
        self, doc: Optional[str]
    ) -> Tuple[List[Tuple[str, str, Union[str, None]]], Optional[str], Optional[str]]:
        args: List[Tuple[str, str, Union[str, None]]] = []
        ret: Optional[str] = None

        try:
            if doc and ":" in doc:
                parts = doc.split(":", 1)
                raw_args = re.sub(r"^.*\( (.*)\) -> *([^ ]+) *$", r"\1, \2", parts[0])
                raw_args = raw_args.replace("[", "").replace("]", "").split(", ")
                ret = raw_args[-1]
                for arg in raw_args[:-1]:
                    arg_parts = re.split("[()]", arg)
                    # Use regex to split by "=" and assign to arg_name and arg_default
                    name_default = re.split(r"=", arg_parts[2].strip(), maxsplit=1)
                    arg_name = name_default[0].strip()
                    arg_type = arg_parts[1].strip()

                    args.append((arg_name, arg_type, None))

                doc = parts[1].strip()
        except Exception as e:
            raise Exception("Error parsing function documentation: {}".format(e))

        return args, ret, doc

    def format_arg(self, arg: Tuple[str, str, Union[str, None]]):
        return f"{arg[0]}: {arg[1]}{'=' + arg[2] if arg[2] is not None else ''}"

    def make_arg_doc(self, args, ret, indent):
        arg_doc = ""
        for arg in args:
            if "=" in arg[0]:
                arg_parts = arg[0].split("=")
                arg_doc = "{0}\n{1}:param {2}: {2} defaults to {4} \n{1}:type {2}: {3}".format(
                    arg_doc, indent, arg_parts[0], arg_parts[1], arg_parts[1]
                )
            else:
                arg_doc = "{0}\n{1}:param {2}: {2}\n{1}:type {2}: {3}".format(
                    arg_doc, indent, arg[0], arg[1]
                )
        if ret:
            arg_doc = "{0}\n{1}:rtype: {2}".format(arg_doc, indent, ret)
        return arg_doc

    def read_file(self, name) -> str:
        with codecs.open(name, "r", "utf-8") as f:
            return f.read()

    def parse_xml(self, file):
        """
        Create and return a namespace-agnostic ElementTree root element.

        :param file: Path to the XML file.
        :return: Root ElementTree.Element or None if parsing fails.
        """
        try:
            text = self.read_file(file)

            it = ElementTree.iterparse(BytesIO(text.encode("UTF-8")))
            for _, el in it:
                if "}" in el.tag:
                    el.tag = el.tag.split("}", 1)[1]  # strip all namespaces
            return it.root  # type: ignore

        except Exception as e:
            print(f"Unexpected error while parsing XML file '{file}': {e}")

        return None
