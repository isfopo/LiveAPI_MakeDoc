# http://remotescripts.blogspot.com

from .MakeDoc import APIMakeDoc
from .types.BuildMode import BuildMode

OUTPUTFOLDER = (
    "%%%OUTPUTFOLDER%%%"  # this is a placeholder value that is replaced at installation
)

BUILDMODE: BuildMode = "%%%BUILDMODE%%%"  # type: ignore


def create_instance(c_instance):
    return APIMakeDoc(c_instance, outdir=OUTPUTFOLDER, build_mode=BUILDMODE)
