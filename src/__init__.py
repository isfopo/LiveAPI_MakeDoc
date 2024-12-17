# http://remotescripts.blogspot.com

from .MakeDoc import APIMakeDoc


def create_instance(c_instance):
    return APIMakeDoc(c_instance)
