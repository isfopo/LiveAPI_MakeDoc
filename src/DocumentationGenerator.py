import inspect
import codecs
import Live


class DocumentationGenerator:
    lines = []
    cssFile: codecs.StreamReaderWriter | None = None
    xmlFile: codecs.StreamReaderWriter | None = None

    def make_doc(self, module, outfilename, cssfilename):
        with codecs.open(cssfilename, "w", "utf-8") as f:
            f.write(self.css)

        if outfilename is not None:
            with codecs.open(outfilename, "w", "utf-8") as f:
                f.write(
                    '<?xml-stylesheet type="text/css" href="Live.css"?>'
                )  # set stylesheet to Live.css
                f.write("<Live>")

                app = Live.Application.get_application()  # get a handle to the App
                maj = app.get_major_version()  # get the major version from the App
                min = app.get_minor_version()  # get the minor version from the App
                bug = app.get_bugfix_version()  # get the bugfix version from the App
                f.write(
                    "Live API version " + str(maj) + "." + str(min) + "." + str(bug)
                )  # main title
                f.write("<Doc>\t%s</Doc>\n" % self.header)
                f.write("<Doc>\t%s</Doc>\n" % self.disclaimer)

                self._describe_module(f, module)

                f.write("</Live>")

    def _get_doc(self, obj):
        """Get object's doc string and remove \n's and clean up <'s and >'s for XML compatibility"""

        doc = False
        if obj.__doc__ is not None:
            doc = (obj.__doc__).replace(
                "\n", ""
            )  # remove newlines from Live API docstings, for wrapped display
            doc = doc.replace(
                "   ", ""
            )  # Strip chunks of whitespace from docstrings, for wrapped display
            doc = doc.replace("<", "&lt;")  # replace XML reserved characters
            doc = doc.replace(">", "&gt;")
            doc = doc.replace("&", "&amp;")
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
            print(f"Warning: No name available for object {obj}. Skipping.")
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
        print(
            "<%s>%s<Description>%s</Description></%s>\n"
            % (description, line_str, description, description)
        )

        # Print the docstring if available
        if hasattr(obj, "__doc__") and obj.__doc__:
            print("<Doc>\t%s</Doc>\n" % self._get_doc(obj))

    def _describe_obj(self, descr: str, obj):
        """Describe object passed as argument, and identify as Class, Method, Property, Value, or Built-In"""

        # Safely get the name attribute if it exists
        obj_name = getattr(obj, "__name__", None)
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
            members = inspect.getmembers(obj)

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

            # # Process non-callable, non-class attributes (Values)
            # for name, member in members:
            #     if not (
            #         inspect.isbuiltin(member)
            #         or inspect.isclass(member)
            #         or inspect.ismethod(member)
            #         or inspect.isfunction(member)
            #     ):
            #         _print_obj_info("Value", member, name)
            #         if self.lines:
            #             self.lines.pop()

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
            print(f"<Error> Error processing object {obj}: {e} </Error>")
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

    header = """Unofficial Live API documentation generated by the "API_MakeDoc" MIDI Remote Script.   
                <requirement xmlns:html="http://www.w3.org/1999/xhtml"></requirement>
                """
    disclaimer = """This is unofficial documentation. Please do not contact Ableton with questions or problems relating to the use of this documentation."""

    css = """/* Style Sheet for formatting XML output of Live API Inspector */
        Live
        {
        background: #f8f8f8;
        display: block;
        margin-bottom: 10px;
        margin-left: 20px;
        margin-top: 10px;
        padding: 4px;
        font-family: "Lucida Sans Unicode", "Lucida Sans", "Lucida Grande", Verdana, sans-serif;
        font-weight: bold;
        color: #000000;
        font-size: 10pt;
        } 

        Module, Class, Sub-Class
        {
        display: block;
        margin-bottom: 5px;
        margin-top: 10px;
        margin-left: -5px;
        padding-left: 5px;
        padding-top: 4px;
        padding-bottom: 4px;
        background: silver;
        font-size: 12pt;
        background-color: #DDD;
        border: solid 1px #AAA;
        color: #333;
        }

        Module
        {
        display: block;
        color: #000;
        background-color: #CCC;
        }

        Description
        {
        display: inline;
        margin-left: 5px;
        color: #000000;
        font-family: Arial, Helvetica, sans-serif;
        font-style: italic;
        font-weight: normal;
        font-size: 9pt;
        }

        Doc
        {
        display: block;
        color: #408080;
        margin-left: 20pt;
        font-family: Arial, Helvetica, sans-serif;
        font-style: italic;
        font-weight: normal;
        font-size: 9pt;
        }
        Method 
        {
        display: block;
        margin-top: 10px;
        color: #000080;
        }
        Built-In 
        {		
        display: block;
        margin-top: 10px;
        color: #081798;
        }
        Property 
        {
        display: block;
        margin-top: 10px;
        color: #0000AF;
        }
        Value 
        {
        display: block;
        margin-top: 10px;
        color: #1C5A8D;
        }
        """