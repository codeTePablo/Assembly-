from tkinter import *
from tkinter import filedialog
from tuples import *
from functions import *
from expresionesRegulares import *
from codeSegementlines import *
from anlisisVariables import *

labels = []


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


def checkLinewithoutOperands(line, n):
    line = line.replace(",", " ")
    line = line.split(" ")
    if len(line) > 1:
        word = " ".join(line)
        print(f"{n} - {word} :error : esta instruccion  no admite operandos")
    else:
        word = " ".join(line)
        print(f"{n}- {(word)} :linea correcta")
    pass


def analizeCodeSegment(codeSegment, tuplaVariables8bits, tuplaVariables16bits, n):
    print(f"{n+1} - code segment :linea correcta")
    for n, line in enumerate(codeSegment, start=n + 2):
        if line.startswith(instrucciones_sin_operando):
            line = cleanLine(line)
            checkLinewithoutOperands(line, n)
        elif line.startswith(instrucciones_con_operandos):
            if (
                analyzeOperandsCodeSegments(
                    line, tuplaVariables8bits, tuplaVariables16bits, n
                )
                == True
            ):
                print(f"{n} - {line} :linea correcta")
            else:
                pass
        elif line.startswith(instruccionconDosOperandos):
            if (
                analyzeTwoOperandsCodeSegments(
                    line, tuplaVariables8bits, tuplaVariables16bits, n
                )
                == True
            ):
                print(f"{n} - {line} :linea correcta")
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
            if (CheckingEtiqueta(line)) == True:
                print(f"{n} - {line} : es una etiqueta")
                line = line.replace(":", "")
                labels.append([line])

            elif (CheckingEtiqueta(line)) == False:
                print(f"{n} - {line} parametros incorrectos")
        else:
            print(f"{n}- {line} es un error")
    print(f"{n+1} - ends :linea correcta")


raw_file = open_file()
clean_file = clear_File(raw_file)
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


variables8bits, variables16bits, n = AnalyzerDataSegment(data_seccion)

variables8BitsN, variables16BitsN = CleanVariables(variables8bits, variables16bits)

tuplaVariables8bits = tuple(variables8BitsN)
tuplaVariables16bits = tuple(variables16BitsN)

n = analyzeStackSegment(stack_seccion, n)

analizeCodeSegment(code_seccion, tuplaVariables8bits, tuplaVariables16bits, n)


tableVariables = variables8BitsN + variables16BitsN

CreateTableVariables(tableVariables, labels)
