from tkinter import *
from tkinter import filedialog
from tuples import *
from functions import *
from expresionesRegulares import *

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
    try:
        indexofDataSegment = clean_file.index("data segment")
        indexofDataSegmentEnds = clean_file.index("ends")
        seccionData = clean_file[indexofDataSegment + 1 : indexofDataSegmentEnds]
        return seccionData, indexofDataSegmentEnds
    except:
        print("Error fatal No se encontro la seccion de data segment")
        exit()


def searchStacksSegments(clean_file):
    try:
        indexofStacksSegment = clean_file.index("stack segment")
        indexofStacksSegmentEnds = clean_file.index("ends")
        seccionStacks = clean_file[indexofStacksSegment + 1 : indexofStacksSegmentEnds]

        return seccionStacks, indexofStacksSegmentEnds
    except:
        print("Error fatal No se encontro la seccion de stack segment")
        exit()


def searchCodeSegment(clean_file):
    try:
        inexofCodeSegment = clean_file.index("code segment")
        inexofCodeSegmentEnds = clean_file.index("ends")
        seccionCode = clean_file[inexofCodeSegment + 1 : inexofCodeSegmentEnds]

        return seccionCode, inexofCodeSegmentEnds, inexofCodeSegment
    except:
        print("Error fatal No se encontro la seccion de code segment")
        exit()


def checkLinewithoutOperands(line, n):
    line = line.replace(",", " ")
    line = line.split(" ")
    if len(line) > 1:
        word = " ".join(line)
        print(f"{n}- {word} :error : parametros incorrectos")
    else:
        word = " ".join(line)
        print(f"{n}- {(word)} :linea correcta")
    pass


def analizeCodeSegment(dataSegment, n):
    print(f"{n+1}- code segment :linea correcta")
    for n, line in enumerate(dataSegment, start=n + 2):
        if line.startswith(instrucciones_sin_operando):
            line = cleanLine(
                line
            )  # Se limpia la linea de esapcios antes y despues de la linea y se quitan las comas
            checkLinewithoutOperands(line, n)  # Se analiza la linea
        elif line.startswith(instruccionesTuplas):
            print(f"{n}- {line} es una instruccion con operando")
            check_order_istructions(create_list_for_instructions(line))
        elif line.startswith(OtrasInstrucciones):
            print(f"{n}- {line} es una que empieza con instrucciones que no nos toca")
        elif line.startswith(numbers):
            print(f"{n}- {line} parametros incorrectos")
        elif line.endswith(":"):
            # Se busca una linea que termine con dos puntos y se analiza si esta correcta o no
            if (CheckingEtiqueta(line)) == True:
                print(f"{n}- {line} es una etiqueta")
            elif (CheckingEtiqueta(line)) == False:
                print(f"{n}- {line} parametros incorrectos")
        else:
            print(f"{n}- {line} es un error")


raw_file = open_file()
print(raw_file)


clean_file = clear_File(raw_file)

# print(clean_file) # Lista de lineas limpias separadas por comas dentro de una lista

dataSegment, indexOfends = searchDataSegment(clean_file)

del clean_file[0 : indexOfends + 1]
stackSegment, indexOfends = searchStacksSegments(clean_file)
AnalyzeStackSegment(stackSegment)

del clean_file[0 : indexOfends + 1]
codeSegmet, indexOfends, indexOfstart = searchCodeSegment(clean_file)

# Esta funcion analiza el data segment y devuelve una lista de listas con las variables y sus tipos y el numero de linea
variables, n = AnalyzerDataSegment(dataSegment)
# print(variables) <---- con esa "variables" debemos crear un diccionario o algo para el nombre de variable y su tipo para buscarlas cuando se ejecute una instrucción con una variable
# Esta funcion analiza el stack segment y devuelve una lista de listas con las variables y sus tipos y el numero de linea
analizeCodeSegment(codeSegmet, n)
