import inspect
from codecs import StreamReaderWriter
from typing import Union
import sys
import os

from ..helpers.app import get_version_number
from .Generator import Generator


class DocumentationGenerator(Generator):
    lines = []

    def __init__(self, module, outdir, script_dir):
        super().__init__(
            module,
            outdir,
            script_dir,
            os.path.join(outdir, str(module.__name__) + ".xml"),
        )

    def make_doc(self, module):
        self.write(self.header)
        self.write("<Root><Live>")

        self.write(
            f"<Header>Live API Version {get_version_number(module)}</Header>"
        )  # main title

        self.write(f"<Doc>Running Python version {sys.version.split(' ')[0]}</Doc>\n")

        self.write(f"<Doc>\t{self.disclaimer}</Doc>\n")

        self._describe_module(self.file, module)

        self.write("</Live></Root>")

        self.xmlFile = None

    def _get_doc(self, obj):
        """Get object's doc string and remove \n's and clean up <'s and >'s for XML compatibility"""

        if getattr(obj, "__doc__") is not None:
            return self._clean_doc(getattr(obj, "__doc__"))

    def _clean_doc(self, doc):
        """Remove \n's and clean up <'s and >'s for XML compatibility"""

        doc = doc.replace(
            "\n", ""
        )  # remove newlines from Live API docstings, for wrapped display
        doc = doc.replace(
            "   ", ""
        )  # Strip chunks of whitespace from docstrings, for wrapped display
        doc = doc.replace("&", "&amp;")
        doc = doc.replace("<", "&lt;")  # replace XML reserved characters
        doc = doc.replace(">", "&gt;")
        return doc

    def _print_obj_info(self, description, obj, name=None):
        """Print object's descriptor and name on one line, and docstring (if any) on the next"""

        # Safely retrieve __name__ if it exists
        obj_name = getattr(obj, "__name__", None)

        # Filter out unnamed Boost.Python functions and special methods
        if obj_name:
            if obj_name == "<unnamed Boost.Python function>" or obj_name.startswith(
                "__"
            ):
                return

        # Determine the name to use
        name_str = obj_name if obj_name is not None else name

        # Proceed only if name_str is available
        if name_str is None:
            self.write(f"Warning: No name available for object {obj}. Skipping.")
            return

        # Handle self.lines stack
        if len(self.lines) != 0:
            assert name_str is not None

            self.lines.append("." + name_str)
            if inspect.ismethod(obj) or inspect.isbuiltin(obj):
                self.lines[-1] += "()"
        else:
            self.lines.append(name_str)

        # Build the line string
        line_str = "".join(self.lines)

        # Print the formatted description
        self.write(
            "<%s>%s<Description>%s</Description></%s>\n"
            % (description, line_str, description, description)
        )

        # Print the docstring if available
        if hasattr(obj, "__doc__") and getattr(obj, "__doc__"):
            self.write(f"<Doc>\t{self._get_doc(obj)}</Doc>\n")

    def _describe_obj(self, descr: str, obj):
        """Describe object passed as argument, and identify as Class, Method, Property, Value, or Built-In"""

        # Attempt to get object name via __name__ or __qualname__
        obj_name = getattr(obj, "__name__", getattr(obj, "__qualname__", None))

        if obj_name:
            # Filter out unnamed Boost.Python functions and special methods
            if obj_name == "<unnamed Boost.Python function>" or obj_name.startswith(
                "__"
            ):
                return
            # Filter out non-subclass 'type' and 'class' types
            if obj_name in ("type", "class"):
                return

            # Output initial object information
            self._print_obj_info(descr, obj)

        # If the object is a method or built-in, stop further processing
        if inspect.ismethod(obj) or inspect.isbuiltin(obj):
            if self.lines:
                self.lines.pop()
            return

        try:
            # Retrieve all members of the object
            members = [(name, getattr(obj, name)) for name in dir(obj)]

            # Process properties
            for name, member in members:
                if isinstance(member, property):
                    self._print_obj_info("Property", member, name)
                    if self.lines:
                        self.lines.pop()

            # Process methods and functions
            for name, member in members:
                if inspect.isbuiltin(member) or inspect.isfunction(member):
                    self._describe_obj("Method", member)

            # Process subclasses of the current object
            for name, member in members:
                if inspect.isclass(member):
                    # Check if 'member' is a subclass of 'obj'
                    try:
                        if issubclass(member, obj):
                            self._describe_obj("Sub-Class", member)
                        else:
                            self._describe_obj("Class", member)
                    except TypeError:
                        # 'obj' is not a class, so cannot be a base class
                        self._describe_obj("Class", member)

            if self.lines:
                self.lines.pop()

        except Exception as e:
            # Log the exception with more detail
            self.write(f"<Error> Error processing object {obj}: {e} </Error>")
            return

    def _describe_module(self, f: Union[StreamReaderWriter, None], module):
        """
        Describe the module object passed as argument
        including its root classes and functions
        """

        self._print_obj_info("Module", module)

        for name in dir(module):  # do the built-ins first
            obj = getattr(module, name)
            if inspect.isbuiltin(obj):
                self._describe_obj("Built-In", obj)

        for name in dir(module):  # then the rest
            obj = getattr(module, name)
            if inspect.isclass(obj):
                self._describe_obj("Class", obj)
            elif inspect.ismethod(obj) or inspect.isfunction(obj):
                self._describe_obj("Method", obj)
            elif inspect.ismodule(obj):
                self._describe_module(f, obj)

        self.lines.pop()

    header = """<?xml-stylesheet type="text/css" href="../Live.css"?>"""

    disclaimer = """Unofficial Live API documentation generated by the "API_MakeDoc" MIDI Remote Script.
    This is unofficial documentation. Please do not contact Ableton with questions or problems relating to the use of this documentation."""
