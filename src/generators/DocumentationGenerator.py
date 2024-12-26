import http.server
import inspect
import codecs
import socketserver
import sys
import os
import http
import threading
from typing import Any, Callable, Union

from ..types.BuildMode import BuildMode
from ..helpers.app import get_version_number


class DocumentationGenerator:
    module: Any
    outdir: str
    script_dir: str
    xmlfilename: str
    lines = []
    xmlFile: Union[codecs.StreamReaderWriter, None] = None
    port: int
    on_server_start: Union[Callable[[int], None], None]
    httpd: socketserver.TCPServer
    build_mode: BuildMode

    def __init__(
        self,
        module,
        outdir,
        script_dir,
        build_mode: BuildMode,
        port=8080,
        on_server_start: Union[Callable[[int], None], None] = None,
    ):
        self.module = module
        self.outdir = outdir
        self.script_dir = script_dir
        self.build_mode = build_mode
        self.port = port
        self.on_server_start = on_server_start

    def generate(self):
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

        self.make_doc(self.module)

    def make_doc(self, module):
        self.xmlfilename = os.path.join(self.outdir, str(module.__name__) + ".xml")

        if self.xmlfilename is not None:
            with codecs.open(self.xmlfilename, "w", "utf-8") as f:
                self.xmlFile = f

                self._write_to_xml(
                    '<?xml-stylesheet type="text/css" href="../Live.css"?>\n'
                )  # set stylesheet to Live.css
                self._write_to_xml("<Live>")

                self._write_to_xml(
                    "Live API version " + get_version_number(module)
                )  # main title

                self._write_to_xml(
                    "<Doc>Running Python version %s</Doc>\n" % sys.version.split(" ")[0]
                )

                self._write_to_xml("<Doc>\t%s</Doc>\n" % self.header)

                self._write_to_xml("<Doc>\t%s</Doc>\n" % self.disclaimer)

                self._describe_module(f, module)

                self._write_to_xml("</Live>")

                self.xmlFile = None

            if self.build_mode != BuildMode.Build:
                self.server_thread = threading.Thread(
                    target=self._start_http_server, daemon=True
                )
                if self.on_server_start is not None:
                    self.on_server_start(self.port)
                self.server_thread.start()

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
        if obj_name:
            name_str = obj_name
        else:
            name_str = name

        # Proceed only if name_str is available
        if name_str is None:
            self._write_to_xml(
                f"Warning: No name available for object {obj}. Skipping."
            )
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
        self._write_to_xml(
            "<%s>%s<Description>%s</Description></%s>\n"
            % (description, line_str, description, description)
        )

        # Print the docstring if available
        if hasattr(obj, "__doc__") and getattr(obj, "__doc__"):
            self._write_to_xml("<Doc>\t%s</Doc>\n" % self._get_doc(obj))

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
            self._write_to_xml(f"<Error> Error processing object {obj}: {e} </Error>")
            return

    def _describe_module(self, f, module):
        """Describe the module object passed as argument
        including its root classes and functions"""

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

    def _write_to_xml(self, text: str) -> None:
        if text is not None and self.xmlFile is not None:
            self.xmlFile.write(text)

    @staticmethod
    def is_boost_python(obj):
        return hasattr(obj, "__module__") and "boost.python" in obj.__module__

    def _start_http_server(self):
        """Start a simple HTTP server to host Live.xml"""

        # Change the current working directory to the output directory
        os.chdir(self.outdir)

        handler = http.server.SimpleHTTPRequestHandler

        with socketserver.TCPServer(("", self.port), handler) as httpd:
            self.httpd = httpd
            try:
                httpd.serve_forever()
            except Exception:
                httpd.server_close()

    def close(self):
        self.httpd.server_close()

    header = """Unofficial Live API documentation generated by the "API_MakeDoc" MIDI Remote Script.   
                <requirement xmlns:html="http://www.w3.org/1999/xhtml"></requirement>
                """
    disclaimer = """This is unofficial documentation. Please do not contact Ableton with questions or problems relating to the use of this documentation."""
