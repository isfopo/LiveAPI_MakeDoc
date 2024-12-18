# http://remotescripts.blogspot.com

from .MakeDoc import APIMakeDoc

OUTPUTFOLDER = "%%%OUTPUTFOLDER%%%"


def create_instance(c_instance):
    return APIMakeDoc(c_instance, out_dir=OUTPUTFOLDER)
