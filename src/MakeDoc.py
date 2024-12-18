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
"""

import Live  # type: ignore
from _Framework.ControlSurface import ControlSurface  # type: ignore
from .generators.StubGenerator import StubGenerator
from .generators.DocumentationGenerator import DocumentationGenerator


class APIMakeDoc(ControlSurface):
    outdir: str
    document_gen: DocumentationGenerator

    def __init__(self, c_instance, out_dir):
        ControlSurface.__init__(self, c_instance)
        self.outdir = out_dir
        self.build_documentation()
        self.build_stub()

    def build_documentation(self):
        self.log_message("Generating documentation for Live API")

        self.document_gen = DocumentationGenerator(
            Live, self.outdir, on_server_start=self.handle_on_server_start
        )

        self.log_message("Completed Generating documentation for Live API")

    def build_stub(self):
        self.log_message("Generating stub for Live API")
        stub_generator = StubGenerator()
        stub_generator.generate(self.outdir)
        self.log_message("Completed generating stub for Live API")

    def handle_on_server_start(self, port: int):
        self.show_message(
            "Documentation is being served at localhost:%s/Live.xml" % port
        )

    def disconnect(self):
        self.document_gen.close()
        ControlSurface.disconnect(self)
