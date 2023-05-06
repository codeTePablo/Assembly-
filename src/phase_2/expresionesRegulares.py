import re
from tuples import *
from prettytable import PrettyTable


def CheckingEtiqueta(etiqueta):
    patron = r"^(?P<etiqueta>[a-zA-Z_]\w*\s*):$"
    coincidencias = re.search((patron), etiqueta)
    if coincidencias:
        return True
    else:
        return False
