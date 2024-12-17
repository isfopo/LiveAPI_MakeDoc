# http://remotescripts.blogspot.com

"""
Copyright (C) 2011 Hanz Petrov <hanz.petrov@gmail.com>
MIDI Remote Script for generating Live API documentation,
based on realtime inspection of the Live module.
Writes two files to the userhome directory - Live.xml and Live.css.

Inspired in part by the following Live API exploration modules:
dumpXML by Nathan Ramella http://code.google.com/p/liveapi/source/browse/trunk/docs/Ableton+Live+API/makedocs
and LiveAPIGen by Patrick Mueller http://muellerware.org

Parts of the describe methods are based on "describe" by Anand, found at:
http://code.activestate.com/recipes/553262-list-classes-methods-and-functions-in-a-module/

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import Live
from _Framework.ControlSurface import ControlSurface
import os
import sys
import inspect
import stub


class APIMakeDoc(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        module = Live
        outdir = os.path.expanduser("~")
        outfilename = str(module.__name__) + ".xml"
        outfilename = os.path.join(outdir, outfilename)
        cssfilename = "Live.css"
        cssfilename = os.path.join(outdir, cssfilename)
        make_doc(module, outfilename, cssfilename)
        stub.generate(Live, outdir)

    def disconnect(self):
        ControlSurface.disconnect(self)


def make_doc(module, outfilename, cssfilename):
    if outfilename is not None:
        stdout_old = sys.stdout

        outputfile = open(cssfilename, "w")
        sys.stdout = outputfile
        print(css)
        outputfile.close()

        outputfile = open(outfilename, "w")
        sys.stdout = outputfile

        print(
            '<?xml-stylesheet type="text/css" href="Live.css"?>'
        )  # set stylesheet to Live.css
        print("<Live>")

        app = Live.Application.get_application()  # get a handle to the App
        maj = app.get_major_version()  # get the major version from the App
        min = app.get_minor_version()  # get the minor version from the App
        bug = app.get_bugfix_version()  # get the bugfix version from the App
        print(
            "Live API version " + str(maj) + "." + str(min) + "." + str(bug)
        )  # main title
        print("<Doc>\t%s</Doc>\n" % header)
        print("<Doc>\t%s</Doc>\n" % disclaimer)

        describe_module(module)

        print("</Live>")
        outputfile.close()
        sys.stdout = stdout_old


def get_doc(obj):
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


def print_obj_info(description, obj, name=None):
    """Print object's descriptor and name on one line, and docstring (if any) on the next"""

    # Safely retrieve __name__ if it exists
    obj_name = getattr(obj, "__name__", None)

    # Filter out unnamed Boost.Python functions and special methods
    if obj_name:
        if obj_name == "<unnamed Boost.Python function>" or obj_name.startswith("__"):
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

    # Handle LINE stack
    if len(LINE) != 0:
        assert name_str is not None

        LINE.append("." + name_str)
        if inspect.ismethod(obj) or inspect.isbuiltin(obj):
            LINE[-1] += "()"
    else:
        LINE.append(name_str)

    # Build the line string
    line_str = "".join(LINE)

    # Print the formatted description
    print(
        "<%s>%s<Description>%s</Description></%s>\n"
        % (description, line_str, description, description)
    )

    # Print the docstring if available
    if hasattr(obj, "__doc__") and obj.__doc__:
        print("<Doc>\t%s</Doc>\n" % get_doc(obj))


def describe_obj(descr: str, obj):
    """Describe object passed as argument, and identify as Class, Method, Property, Value, or Built-In"""

    # Safely get the name attribute if it exists
    obj_name = getattr(obj, "__name__", None)
    if obj_name:
        # Filter out unnamed Boost.Python functions and special methods
        if obj_name == "<unnamed Boost.Python function>" or obj_name.startswith("__"):
            return
        # Filter out non-subclass 'type' and 'class' types
        if obj_name in ("type", "class"):
            return

        # Output initial object information
        print_obj_info(descr, obj)

    # If the object is a method or built-in, stop further processing
    if inspect.ismethod(obj) or inspect.isbuiltin(obj):
        if LINE:
            LINE.pop()
        return

    try:
        # Retrieve all members of the object
        members = inspect.getmembers(obj)

        # Process properties
        for name, member in members:
            if isinstance(member, property):
                print_obj_info("Property", member, name)
                if LINE:
                    LINE.pop()

        # Process methods and functions
        for name, member in members:
            if inspect.isbuiltin(member) or inspect.isfunction(member):
                describe_obj("Method", member)

        # # Process non-callable, non-class attributes (Values)
        # for name, member in members:
        #     if not (
        #         inspect.isbuiltin(member)
        #         or inspect.isclass(member)
        #         or inspect.ismethod(member)
        #         or inspect.isfunction(member)
        #     ):
        #         print_obj_info("Value", member, name)
        #         if LINE:
        #             LINE.pop()

        # Process subclasses of the current object
        for name, member in members:
            if inspect.isclass(member):
                # Check if 'member' is a subclass of 'obj'
                try:
                    if issubclass(member, obj):
                        describe_obj("Sub-Class", member)
                    else:
                        describe_obj("Class", member)
                except TypeError:
                    # 'obj' is not a class, so cannot be a base class
                    describe_obj("Class", member)

        if LINE:
            LINE.pop()

    except Exception as e:
        # Log the exception with more detail
        print(f"<Error> Error processing object {obj}: {e} </Error>")
        return


def describe_module(module):
    """Describe the module object passed as argument
    including its root classes and functions"""

    print_obj_info("Module", module)

    for name in dir(module):  # do the built-ins first
        obj = getattr(module, name)
        if inspect.isbuiltin(obj):
            describe_obj("Built-In", obj)

    for name in dir(module):  # then the rest
        obj = getattr(module, name)
        if inspect.isclass(obj):
            describe_obj("Class", obj)
        elif inspect.ismethod(obj) or inspect.isfunction(obj):
            describe_obj("Method", obj)
        elif inspect.ismodule(obj):
            describe_module(obj)
    if LINE:
        LINE.pop()


LINE = []

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
