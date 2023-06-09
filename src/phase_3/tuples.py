OtrasInstrucciones = (
    "AAM",
    "CBW",
    "CLD",
    "CMC",
    "CMPSW",
    "DAA",
    "AAS",
    "CLC",
    "CLI",
    "CMPSB",
    "CWD",
    "DAS",
    "IRET",
    "LODSB",
    "MOVSB",
    "NOP",
    "POPF",
    "PUSHF",
    "LAHF",
    "LODSW",
    "MOVSW",
    "POPA",
    "PUSHA",
    "RET",
    "STD",
    "STOSB",
    "XLATB",
    "STI",
    "STOSW",
    "INT",
    "MUL",
    "NEG",
    "NOT",
    "IMUL",
    "IDIV",
    "INC",
    "PUSH",
    "IDIV",
    "IDIV",
    "INC",
    "PUSH",
    "IDIV",
    "NOT",
    "IMUL",
    "MUL",
    "NEG",
    "DIV",
    "RCL",
    "ADD",
    "ROR",
    "AND",
    "SAR",
    "SHL",
    "SUB",
    "LEA",
    "TEST",
    "XCHG",
    "MOV",
    "XOR",
    "OR",
    "JNA",
    "JNS",
    "JAE",
    "JNAE",
    "JNZ",
    "JB",
    "JNC",
    "JS",
    "JCXZ",
    "JNE",
    "JZ",
    "JE",
    "JNL",
    "LOOPNE",
    "JL",
    "JNLE",
    "LOOPNZ",
    "JLE",
    "JO",
    "JG",
    "JNGE",
    "LOOPE",
    "LOOP",
    "JMP",
    "JNP",
    "JBE",
    "JNBE",
    "JP",
    "aam",
    "cbw",
    "cld",
    "cmc",
    "cmpsw",
    "daa",
    "aas",
    "clc",
    "cli",
    "cmpsb",
    "cwd",
    "das",
    "iret",
    "lodsb",
    "movsb",
    "nop",
    "popf",
    "pushf",
    "lahf",
    "lodsw",
    "movsw",
    "popa",
    "pusha",
    "ret",
    "std",
    "stosb",
    "xlatb",
    "sti",
    "stosw",
    "int",
    "mul",
    "neg",
    "dec",
    "not",
    "imul",
    "idiv",
    "inc",
    "push",
    "idiv",
    "idiv",
    "inc",
    "push",
    "idiv",
    "not",
    "imul",
    "mul",
    "neg",
    "dec",
    "div",
    "rcl",
    "add",
    "ror",
    "and",
    "sar",
    "shl",
    "sub",
    "lea",
    "test",
    "les",
    "xchg",
    "mov",
    "xor",
    "or",
    "jna",
    "jns",
    "jae",
    "jnae",
    "jnz",
    "jb",
    "jnc",
    "js",
    "jcxz",
    "jne",
    "jz",
    "je",
    "jnl",
    "loopne",
    "jl",
    "jnle",
    "loopnz",
    "jle",
    "jo",
    "jg",
    "jnge",
    "loope",
    "loop",
    "jmp",
    "jnp",
    "jbe",
    "jnbe",
    "jp",
)

numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


registros16bits = (
    "AX",
    "BX",
    "CX",
    "DS",
    "DX",
    "DI",
    "SI",
    "si",
    "di" ,
    "ax",
    "bx",
    "cx",
    "dx",
    "ds",
)

registros8bits = (
    "AL",
    "AH",
    "BL",
    "BH",
    "CL",
    "CH",
    "DL",
    "DH",
    "al",
    "ah",
    "bl",
    "bh",
    "cl",
    "ch",
    "dl",
    "dh",
)



registros_de_segmento = (
    "ES",
    "CS",
    "SS",
    "DS",
)

instrucciones_con_operandos = (
    "ADC",
    "CMP",
    "adc",
    "cmp",
)


instruccionconDosOperandos = (
    "LES",
    "LDS",
    "les",
    "lds",
)
instrucciones_con_un_operando = (
    "DEC",
    "IDIV",
    "IMUL",
    "POP",
    "dec",
    "idiv",
    "imul",
    "pop",
)

instrucciondeSaltos = (
    "JA",
    "JC",
    "JGE",
    "JNB",
    "JNG",
    "JNO",
    "ja",
    "jc",
    "jge",
    "jnb",
    "jng",
    "jno",
)

instrucciones_sin_operando = (
    "AAA",
    "AAD",
    "HLT",
    "INTO",
    "SCASW",
    "STC",
    "aaa",
    "aad",
    "hlt",
    "into",
    "scasw",
    "stc",
)


pseudoinstruction = (
    "code segment",
    "data segment",
    "stack segment",
    "byte ptr",
    "word ptr",
    "db",
    "dw",
    ".data segment",
    ".code segment",
    ".stack segment",
)

space = (" ", "  ", "", "\n")

data_segment_words = ("EQU", "equ")
data_segment_words_2 = ("dup", "DUP")


dbs = ("db", "DB", "DW", "dw")

equ = ("EQU", "equ")


corchetes = ("[BX + SI]", "[BX + DI]", "[BP + SI]", "[BP + DI]", "[SI]", "[DI]", "[BX]", "[BX+SI]", "[BX+DI]", "[BX+SI]", "[BP+DI]" , "[BP]")

tabla_d = {
    "[BX + SI]": {"mod": "00", "r/m": "000"},
    "[BX + DI]": {"mod": "00", "r/m": "001"},
    "[BP + SI]": {"mod": "00", "r/m": "010"},
    "[BP + DI]": {"mod": "00", "r/m": "011"},
    "[BP]" : {"mod": "01", "r/m": "110"},
    "[BX+SI]": {"mod": "00", "r/m": "000"},
    "[BX+DI]": {"mod": "00", "r/m": "001"},
    "[BP+SI]": {"mod": "00", "r/m": "010"},
    "[BP+DI]": {"mod": "00", "r/m": "011"},
    "[SI]": {"mod": "00", "r/m": "100"},
    "[DI]": {"mod": "00", "r/m": "101"},
    "[BX]": {"mod": "00", "r/m": "111"},
    "BX+SI": {"mod": "00", "r/m": "000"},
    "BX+DI": {"mod": "00", "r/m": "001"},
    "BP+SI": {"mod": "00", "r/m": "010"},
    "BP+DI": {"mod": "00", "r/m": "011"},
    "SI": {"mod": "00", "r/m": "100"},
    "DI": {"mod": "00", "r/m": "101"},
    "BX": {"mod": "00", "r/m": "111"},
    "BP": {"mod": "01", "r/m": "110"},
}

w_es_1 = {
    "AX": {"mod": "11", "r/m": "000"},
    "CX": {"mod": "11", "r/m": "001"},
    "DX": {"mod": "11", "r/m": "010"},
    "BX": {"mod": "11", "r/m": "011"},
    "SP": {"mod": "11", "r/m": "100"},
    "BP": {"mod": "11", "r/m": "101"},
    "SI": {"mod": "11", "r/m": "110"},
    "DI": {"mod": "11", "r/m": "111"},
    "AL": {"mod": "11", "r/m": "000"},
    "CL": {"mod": "11", "r/m": "001"},
    "DL": {"mod": "11", "r/m": "010"},
    "BL": {"mod": "11", "r/m": "011"},
    "AH": {"mod": "11", "r/m": "100"},
    "CH": {"mod": "11", "r/m": "101"},
    "DH": {"mod": "11", "r/m": "110"},
    "BH": {"mod": "11", "r/m": "111"},
}

regs = {
    "ES": {"regs": "00"},
    "CS": {"regs": "01"},
    "SS": {"regs": "10"},
    "DS": {"regs": "11"},
}