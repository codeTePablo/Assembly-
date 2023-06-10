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


saltos = {
    "JA": {"Codificacion": "0F87"},
    "JC": {"Codificacion": "0F82"},
    "JGE": {"Codificacion": "0F8D"},
    "JNB": {"Codificacion": "0F82"},
    "JNG": {"Codificacion": "0F8E"},
    "JNO": {"Codificacion": "0F80"},
}

instrucciones = {
    "PUSH": {"valor": "FF", "direccion": "mod 110 r/m"},
    "POP": {"valor": "10001111", "direccion": "mod 000 r/m"},
    "MUL": {"valor": "1111011w", "direccion": "mod 100 r/m"},
    "IDIV": {"valor": "1111011w", "direccion": "mod 111 r/m"},
    "DEC": {"valor": "1111111w", "direccion": "mod 001 r/m"},
    "IMUL": {"valor": "1111011w", "direccion": "mod 101 r/m"},
}




instrucciones_que_si_fucionan = {
    "LES": {"valor": "11000100" , "direccion": "mod reg r/m"},
    "LDS": {"valor": "11000101" , "direccion": "mod reg r/m"}
}

instrucciones_dos_op_adc = {
    "ADC": {
        "reg_reg": {"valor": "000100dw", "direccion": "mod reg r/m"},
        "mem_reg": {
            "valor": "0001000w",
            "direccion": "mod reg r/m",
            "desplazamiento": "1 o 2",
        },
        "reg_mem": {
            "valor": "0001000w",
            "direccion": "mod reg r/m",
            "desplazamiento": "1 o 2",
        },
        "reg/mem_inm": {
            "valor": "100000sw",
            "direccion": "mod reg r/m",
            "desplazamiento": "1 o 2",
            "inmediato": "1 0 2",
        },
        "acum_inm": {"valor": "0001010w", "inmediato": "1 0 2"},
    }
}
print(instrucciones_dos_op_adc["ADC"]["mem_reg"]["direccion"])


instrucciones_dos_op_cmp = {
    "CMP": {
        "reg_reg": {"valor": "001110dw", "direccion": "mod reg r/m"},
        "mem_reg": {
            "valor": "0011100w",
            "direccion": "mod reg r/m",
            "desplazamiento": "1 o 2",
        },
        "reg_mem": {
            "valor": "0011101w",
            "direccion": "mod reg r/m",
            "desplazamiento": "1 o 2",
        },
        "reg/mem_inm": {
            "valor": "100000sw",
            "direccion": " mod 111 r/m",
            "desplazamiento": "1 o 2",
            "inmediato": "1 0 2",
        }, 
        "acum_inm": {"valor": "0011110w", "inmediato": "1 0 2"},
    }
}


tabla_Reg = {
    "AX": "000",
    "CX": "001",
    "DX": "010",
    "BX": "011",
    "SP": "100",
    "BP": "101",
    "SI": "110",
    "DI": "111",
    "AL": "000",
    "CL": "001",
    "DL": "010",
    "BL": "011",
    "AH": "100",
    "CH": "101",
    "DH": "110",
    "BH": "111"
}