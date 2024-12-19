# http://remotescripts.blogspot.com

from typing import Literal
from .MakeDoc import APIMakeDoc

OUTPUTFOLDER = (
    "%%%OUTPUTFOLDER%%%"  # this is a placeholder value that is replaced at installation
)

BUILDMODE: Literal["build", "submodule"] = "%%%BUILDMODE%%%"  # type: ignore


def create_instance(c_instance):
    return APIMakeDoc(c_instance, outdir=OUTPUTFOLDER, build_mode=BUILDMODE)
