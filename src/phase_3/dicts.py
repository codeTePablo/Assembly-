# diccionoarios para el analizador lexico y sintactico

# listas
REG = [
    "AX",
    "BX",
    "CX",
    "DX",
    "SI",
    "DI",
    "BP",
    "SP",
    "CS",
    "DS",
    "SS",
    "ES",
    "IP",
    "ax",
    "bx",
    "cx",
    "dx",
    "si",
    "di",
    "bp",
    "sp",
    "cs",
    "ds",
    "ss",
    "es",
    "ip",
]

SREG = ["CS", "DS", "SS", "ES"]

immediate = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
label = [""]


# diccionario
def loadDictis(memory):
    instrucciones = {
        "DEC": [(REG, memory)],
        "IDIV": [(REG, memory)],
        "IMUL": [(REG, memory)],
        "ADC": [
            (REG, memory),
            (memory, REG),
            (REG, REG),
            # el inmediate aun no se agrega a la funcion
            (memory, immediate),
            (REG, immediate),
        ],
        "CMP": [
            (REG, memory),
            (memory, REG),
            (REG, REG),
            (memory, immediate),
            (REG, immediate),
        ],
        "LES": [(REG, memory)],
        "LDS": [(REG, memory)],
        "JA": [(label)],
        "JC": [(label)],
        "JGE": [(label)],
        "JNB": [(label)],
        "JNG": [(label)],
        "JNO": [(label)],
    }
    return instrucciones


diccionario_none = {
    "AAA": None,
    "AAD": None,
    "HLT": None,
    "INTO": None,
    "SCASW": None,
    "STC": None,
}


instrucciones= {
    'PUSH': {'valor': 'FF', 'direccion': 'mod 110 r/m'},
    'POP': {'valor': '8F', 'direccion': 'mod 000 r/m'},
    'MUL': {'valor': 'F6', 'direccion': 'mod 100 r/m'},
    'IDIV': {'valor': 'F7', 'direccion': 'mod 111 r/m'},
    'DEC': {'valor': 'FE', 'direccion': 'mod 001 r/m'}
}


saltos ={
    'JA': {'Codificacion': '0F87'},
    'JC': {'Codificacion': '0F82'},
    'JGE': {'Codificacion': '0F8D'},
    'JNB': {'Codificacion': '0F82'},
    'JNG': {'Codificacion': '0F8E'},
    'JNO': {'Codificacion': '0F80'},
}