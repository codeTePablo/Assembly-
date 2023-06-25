from tkinter import *
from tuples import *
from functions import *
from anlisisVariables import *
import keyboard
from analyserCodeSegment import *
from lexicografico import *


def clear_File(file):
    lines = [line.strip().split(";")[0] for line in file.split("\n")]
    lines = [line for line in lines if line]
    clean_lines = []
    for line in lines:
        clean_lines.append(line)
    return clean_lines


def cleanLine(line):
    line = line.replace(",", " ").rstrip().lstrip()
    line = line.replace("  ", "").rstrip().lstrip()
    return line


while True:
    print ("Analisis Lexicografico")
    rw=lexicogtaphic();
   
    print ("----------------------")
    print ("Funcion 3 y 4")
    print ("----------------------")
    clean_file = clear_File(rw)
    try :
        data_section, stack_section, code_section = getSections(clean_file)
    except Exception as e:
        print("Error en el archivo de entrada", e)
        break
    try:
        variables8Bits, variables16Bits, n, count = AnalyzerDataSegment(data_section)
    except Exception as e:
        print("Error en el archivo de entrada", e)
        break

    n, count = analyzeStackSegment(stack_section, n, count)

    tuplaNombreVariables8bits, tuplaNombresVariables16bits = CleanVariables(
        variables8bits, variables16bits
    )


    count = analizeCodeSegment(
        code_section, tuplaNombreVariables8bits, tuplaNombresVariables16bits, variables8bits, variables16bits, n, count
    )

    tableVariables = variables8Bits + variables16Bits
    CreateTableVariables(tableVariables, labels)
    print("Presione ESC para salir")
    keyboard.wait("esc")
    break
