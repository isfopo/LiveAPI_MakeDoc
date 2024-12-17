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

import os
import Live
from _Framework.ControlSurface import ControlSurface
from .stub import generate
from .DocumentationGenerator import DocumentationGenerator


class APIMakeDoc(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        module = Live
        outdir = os.path.expanduser("~")
        outfilename = str(module.__name__) + ".xml"
        outfilename = os.path.join(outdir, outfilename)
        cssfilename = "Live.css"
        cssfilename = os.path.join(outdir, cssfilename)

        document_gen = DocumentationGenerator()

        self.log_message("Generating documentation for Live API")
        document_gen.make_doc(module, outfilename, cssfilename)
        self.log_message("Completed Generating documentation for Live API")

        self.log_message("Generating stub for Live API")
        generate(outdir)
        self.log_message("Completed generating stub for Live API")

    def disconnect(self):
        ControlSurface.disconnect(self)
