from codecs import StreamReaderWriter
import codecs
import inspect
import os
from typing import Any, Union
from abc import abstractmethod


class Generator:
    module: Any
    outdir: str
    script_dir: str
    filepath: str
    file: Union[StreamReaderWriter, None] = None
    header: str
    footer: str

    lines = []

    def __init__(self, module, outdir, script_dir, filepath, header="", footer=""):
        self.module = module
        self.outdir = outdir
        self.script_dir = script_dir
        self.filepath = filepath
        self.header = header
        self.footer = footer

    def generate(self):
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

        if self.filepath is not None:
            self.file = codecs.open(self.filepath, "w", "utf-8")

        self.write(self.header)
        self._describe_module(self.module)
        self.write(self.footer)

        self.close()

    def write(self, text: str) -> None:
        if text is not None and self.file is not None:
            self.file.write(text)

    def close(self):
        """
        Closes the documentation file.
        """
        if self.file is not None:
            self.file.close()
            self.file = None

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

    def _describe_module(self, module):
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
                self._describe_module(obj)

        if self.lines:
            self.lines.pop()

    @abstractmethod
    def _print_obj_info(self, description: str, obj: Any, name=None):
        """Print object's descriptor and name on one line, and docstring (if any) on the next"""
        pass
