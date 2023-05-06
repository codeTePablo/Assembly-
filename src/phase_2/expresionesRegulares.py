import re
from tuples import *


def CheckingEtiqueta(etiqueta):
    patron = r"^(?P<etiqueta>[a-zA-Z_]\w*\s*):$"
    coincidencias = re.search((patron), etiqueta)
    if coincidencias:
        return True
    else:
        return False
