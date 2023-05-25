from tkinter import *
from tuples import *
from functions import *
from anlisisVariables import *
import keyboard
from analyserCodeSegment import *


def clear_File(file):
    lines = [line.strip().split(";")[0] for line in file.split("\n")]
    lines = [line for line in lines if line]
    clean_lines = []
    for line in lines:
        print(line.upper())
        clean_lines.append(line)
    return clean_lines


def cleanLine(line):
    line = line.replace(",", " ").rstrip().lstrip()
    line = line.replace("  ", "").rstrip().lstrip()
    return line


while True:
    raw_file = open_file()
    print(raw_file)
    clean_file = clear_File(raw_file)

    data_section, stack_section, code_section = getSections(clean_file)

    variables8Bits, variables16Bits, n, count = AnalyzerDataSegment(data_section)

    n, count = analyzeStackSegment(stack_section, n, count)

    tuplaNombreVariables8bits, tuplaNombresVariables16bits = CleanVariables(
        variables8bits, variables16bits
    )

    count = analizeCodeSegment(
        code_section, tuplaNombreVariables8bits, tuplaNombresVariables16bits, n, count
    )
    tableVariables = variables8Bits + variables16Bits
    CreateTableVariables(tableVariables, labels)

    print("Presione ESC para salir")
    keyboard.wait("esc")
    break
