from codecs import StreamReaderWriter
import codecs
import os
from typing import Any, Union
from abc import abstractmethod


class Generator:
    module: Any
    outdir: str
    script_dir: str
    filepath: str
    file: Union[StreamReaderWriter, None] = None

    def __init__(self, module, outdir, script_dir, filepath):
        self.module = module
        self.outdir = outdir
        self.script_dir = script_dir
        self.filepath = filepath

    def generate(self):
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

        if self.filepath is not None:
            self.file = codecs.open(self.filepath, "w", "utf-8")

        self.make_doc(self.module)

        self.close()

    @abstractmethod
    def make_doc(self, module):
        """
        Initiates the documentation generation process for the given module.

        Args:
            module (module): the module to document
        """
        pass

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
