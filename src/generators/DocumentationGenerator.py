import inspect
import sys
import os

from ..helpers.app import get_version_number
from .Generator import Generator


class DocumentationGenerator(Generator):
    lines = []

    def __init__(self, module, outdir, script_dir):
        header = f"""
        <?xml-stylesheet type="text/css" href="../Live.css"?>
        <Root>
            <Live>
            <Header>Live API Version {get_version_number(module)}</Header>
            <Doc>
                Running Python version {sys.version.split(' ')[0]}
            </Doc>
            <Doc>
                Unofficial Live API documentation generated by the "API_MakeDoc" MIDI Remote Script.
                This is unofficial documentation. Please do not contact Ableton with questions or problems relating to the use of this documentation
            </Doc>
        """

        footer = """
            </Live>
        </Root>
        """

        super().__init__(
            module,
            outdir,
            script_dir,
            os.path.join(outdir, str(module.__name__) + ".xml"),
            header,
            footer,
        )

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
