from tkinter import *
from tkinter import filedialog
from tuples import *
from functions import *
from expresionesRegulares import *
from codeSegementlines import *
from anlisisVariables import *

# Restructuración de código
labels = []


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
        print(f"{n}- {word} :error : esta instruccion no admite operandos")
    else:
        word = " ".join(line)
        print(f"{n}- {(word)} :linea correcta")
    pass


def analizeCodeSegment(codeSegment, tuplaVariables8bits, tuplaVariables16bits, n):
    print(f"{n+1}- code segment :linea correcta")
    for n, line in enumerate(codeSegment, start=n + 2):
        if line.startswith(instrucciones_sin_operando):
            line = cleanLine(line)
            checkLinewithoutOperands(line, n)  # Se analiza la linea
        elif line.startswith(instrucciones_con_operandos):
            if (
                analyzeOperandsCodeSegments(
                    line, tuplaVariables8bits, tuplaVariables16bits, n
                )
                == True
            ):
                print(f"{n}- {line} :linea correcta")
            else:
                pass
        elif line.startswith(instruccionconDosOperandos):
            if (
                analyzeTwoOperandsCodeSegments(
                    line, tuplaVariables8bits, tuplaVariables16bits, n
                )
                == True
            ):
                print(f"{n}- {line} :linea correcta")
            else:
                pass
        elif line.startswith(instrucciones_con_un_operando):
            if (
                analyzeoneOperandCodeSegments(
                    line, tuplaVariables8bits, tuplaVariables16bits, n
                )
                == True
            ):
                pass
            else:
                pass
        elif line.startswith(instrucciondeSaltos):
            analyceJumps(line, n, labels, tuplaVariables8bits, tuplaVariables16bits)

        elif line.startswith(OtrasInstrucciones):
            print(f"{n}- {line} :insturccion no asignada")
        elif line.startswith(numbers):
            print(f"{n}- {line} error: simbolo no definido")
        elif line.endswith(":"):
            # Se busca una linea que termine con dos puntos y se analiza si esta correcta o no
            if (CheckingEtiqueta(line)) == True:
                print(f"{n}- {line} : es una etiqueta")
                line = line.replace(":", "")
                labels.append([line])

            elif (CheckingEtiqueta(line)) == False:
                print(f"{n}- {line} parametros incorrectos")
        else:
            print(f"{n}- {line} es un error")


raw_file = open_file()
print(raw_file)


clean_file = clear_File(raw_file)

# print(clean_file) # Lista de lineas limpias separadas por comas dentro de una lista
data_seccion = []
stack_seccion = []
code_seccion = []
seccion_actual = None

for linea in clean_file:
    if "data segment" in linea:
        seccion_actual = data_seccion
    elif "stack segment" in linea:
        seccion_actual = stack_seccion
    elif "code segment" in linea:
        seccion_actual = code_seccion
    elif "ends" in linea:
        seccion_actual = None
    elif seccion_actual is not None:
        seccion_actual.append(linea)

# Imprimir las líneas de cada sección


# Esta funcion analiza el data segment y devuelve una lista de listas con las variables y sus tipos y el numero de linea
variables8bits, variables16bits, n = AnalyzerDataSegment2(data_seccion)


variables8BitsN = []
variables16BitsN = []

for elemento in variables8bits:
    if elemento not in variables8BitsN:
        variables8BitsN.append(elemento)


for elemento in variables16bits:
    if elemento not in variables16BitsN:
        variables16BitsN.append(elemento)


memoria8bits = new_list_for_memory(variables8BitsN)
memoria16bits = new_list_for_memory(variables16BitsN)

valores_modificados8bits = []
valores_modificados16bits = []

for elemento in memoria8bits:
    valor = elemento[0]
    valor = valor.replace("[", "").replace("]", "")
    valor = valor.replace("'", "")
    valor = valor.upper()
    valores_modificados8bits.append(valor)


for elemento in memoria16bits:
    valor = elemento[0]
    valor = valor.replace("[", "").replace("]", "")
    valor = valor.replace("'", "")
    valor = valor.upper()
    valores_modificados16bits.append(valor)


tuplaVariables8bits = tuple(valores_modificados8bits)
tuplaVariables16bits = tuple(valores_modificados16bits)


analizeCodeSegment(code_seccion, tuplaVariables8bits, tuplaVariables16bits, n)


tableVariables = []


tableVariables = variables8BitsN + variables16BitsN


for sublista in tableVariables:
    if len(sublista) == 4:
        valor = " ".join(sublista[-2:])
        sublista[-2:] = [valor]

for sublista in tableVariables:
    if sublista[1] in dbs:
        sublista.insert(1, "variable")
    elif sublista[1] == "equ":
        sublista.insert(1, "constante")


for label in labels:
    label.append("etiqueta")
    label.append("Null")
    label.append("Null")

tableVariables = tableVariables + labels
table = PrettyTable(["Simbolo", "Tipo", "Tamaño", "Valor"])

for list in tableVariables:
    table.add_row(list)


print(table)
