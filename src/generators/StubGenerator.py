import os
import re
from typing import Any, List, Optional, Tuple, Union
from .Generator import Generator


class StubGenerator(Generator):
    indent: str = ""

    def __init__(self, module, outdir, script_dir):
        header = "# type: ignore\n"
        header += "from types import ModuleType\n\n"

        super().__init__(
            module,
            outdir,
            script_dir,
            os.path.join(outdir, "Live", "__init__.py"),
            header,
        )

    def _print_obj_info(self, description: str, obj: Any, name=None):
        name = name if name is not None else obj.__name__

        if description == "Module" and name != "Live":
            self.write(f"class {name}(ModuleType):\n")
            self.indent += "    "

        elif description == "Class" or description == "Sub-Class":
            self.write(f"{self.indent}class {name}(object):\n")
            if hasattr(obj, "__doc__"):
                self.write(f"\"\"\"{getattr(obj, '__doc__')}\"\"\"\n")
            self.indent += "    "

        elif description == "Built-In":
            args, ret, doc = self.parse_args_from_doc(getattr(obj, "__doc__"))
            self.write(f"{self.indent}@staticmethod\n")

        #     if args:
        #         self.write(
        #             f"{self.indent}def {name}({', '.join([self.format_arg(arg) for arg in args])}) -> {ret}:\n"
        #         )
        #     else:
        #         self.write(f"{self.indent}def {name}() -> {ret}:")

        #     self.write(
        #         f"\"\"\"{doc}{self.make_arg_doc(args, ret, self.indent + '    ')}\"\"\""
        #     )
        #     self.write("\n")
        #     self.write(f"{self.indent}    pass\n")

    def handle_line_end(self):
        self.indent = self.indent.removesuffix("    ")

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
            raise Exception(f"Error parsing function documentation: {e}")

        return args or [], ret or None, doc or None

    def format_arg(self, arg: Tuple[str, str, Union[str, None]]):
        return f"{arg[0]}: {arg[1]}{'=' + arg[2] if arg[2] is not None else ''}"

    def make_arg_doc(self, args, ret, indent):
        arg_doc = ""
        for arg in args:
            if "=" in arg[0]:
                arg_parts = arg[0].split("=")
                arg_doc = f"{arg_doc}\n{indent}:param {arg_parts[0]}: {arg_parts[0]} defaults to {arg_parts[1]} \n{indent}:type {arg_parts[0]}: {arg_parts[1]}"
            else:
                arg_doc = f"{arg_doc}\n{indent}:param {arg[0]}: {arg[0]}\n{indent}:type {arg[0]}: {arg[1]}"
        if ret:
            arg_doc = f"{arg_doc}\n{indent}:rtype: {ret}"
        return arg_doc
