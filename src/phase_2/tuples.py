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
abecedario = (
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
)
numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

registros = (
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
)


registros16bits = (
    "AX",
    "BX",
    "CX",
    "DX",
    "ax",
    "bx",
    "cx",
    "dx",
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
