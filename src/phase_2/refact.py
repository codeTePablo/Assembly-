from tkinter import *
from tkinter import filedialog
from tuples import *
from functions import *
from prettytable import PrettyTable

# Restructuración de código


# Open file
def open_file():
    """Abre el archivo y lo lee"""
    filepath = filedialog.askopenfilename(
        filetypes=[("ASM", "*.asm*"), ("Text Files", "*.txt")]
    )
    file = open(filepath, "r")

    return file.read()


def clear_File(file):
    lines = [line.strip().split(";")[0] for line in file.split("\n")]
    lines = [line for line in lines if line]

    clean_lines = []
    for line in lines:
        clean_lines.append(line)
    return clean_lines


def cleanLine(line):
    line = line.replace(",", " ").rstrip().lstrip()
    return line


def searchDataSegment(clean_file):
    indexofDataSegment = clean_file.index("data segment")
    indexofDataSegmentEnds = clean_file.index("ends")
    seccionData = clean_file[indexofDataSegment + 1 : indexofDataSegmentEnds]

    return seccionData, indexofDataSegmentEnds


def searchStacksSegments(clean_file):
    indexofStacksSegment = clean_file.index("stack segment")
    indexofStacksSegmentEnds = clean_file.index("ends")
    seccionStacks = clean_file[indexofStacksSegment + 1 : indexofStacksSegmentEnds]

    return seccionStacks, indexofStacksSegmentEnds


def searchCodeSegment(clean_file):
    inexofCodeSegment = clean_file.index("code segment")
    inexofCodeSegmentEnds = clean_file.index("ends")
    seccionCode = clean_file[inexofCodeSegment + 1 : inexofCodeSegmentEnds]

    return seccionCode, inexofCodeSegmentEnds


def analizeDataSegment(dataSegment):
    pass


def checkLinewithoutOperands(line):
    line = line.replace(",", " ")
    line = line.split(" ")
    if len(line) > 1:
        word = " ".join(line)
        print(f"{word} :error : parametros incorrectos")
    else:
        word = " ".join(line)
        print(f"{(word)} :linea correcta")
    pass


def analizeCodeSegment(dataSegment):
    for line in dataSegment:
        if line.startswith(instrucciones_sin_operando):
            line = cleanLine(line)
            checkLinewithoutOperands(line)
        elif line.startswith(instrucciones):
            print(f"{line} es una instruccion con operando")
        elif line.startswith(OtrasInstrucciones):
            print(f"{line} es una que empieza con instrucciones que no nos toca")
        elif line.startswith(numbers):
            print(f"{line} parametros incorrectos")
        elif line.endswith(":"):
            print(f"{line} es una etiqueta")
        else:
            print(f"{line} es un error")


# Se almacena el archivo crudo en una variable
raw_file = open_file()
raw_file.capitalize
print(raw_file)


# El archivo crudo se limpia y se almacena en la variable clean_file
clean_file = clear_File(raw_file)

# Se identifica el segmento de datos
dataSegment, indexOfends = searchDataSegment(clean_file)

del clean_file[0 : indexOfends + 1]
# Se identifica el segmento de stacks
stackSegment, indexOfends = searchStacksSegments(clean_file)

del clean_file[0 : indexOfends + 1]
# Se identifica el segmento de código
codeSegmet, indexOfends = searchCodeSegment(clean_file)
analizeCodeSegment(codeSegmet)

# print("Segmento de datos")
# print(dataSegment)
# print("Segmento de stack")
# print(stackSegment)
# print("Segmento de código")
# print(codeSegmet)