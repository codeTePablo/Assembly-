from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tuples import *
from functions import *
from expresionesRegulares import *
from codeSegementlines import *
from anlisisVariables import *
import keyboard


labels = []


def open_file():
    """Abre el archivo y lo lee"""

    try:
        filepath = filedialog.askopenfilename(
            filetypes=[("ASM", "*.asm*"), ("Text Files", "*.txt")]
        )
        file = open(filepath, "r")
        return file.read()
    except Exception as e:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", "Error al abrir el archivo: " + str(e))


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


def checkLinewithoutOperands(line, n, count):
    line = line.replace(",", " ")
    line = line.split(" ")
    if len(line) > 1:
        word = " ".join(line)
        print(
            f"{n} -  {count:x}H - {word} :error : esta instruccion  no admite operandos"
        )
        return count
    else:
        word = " ".join(line)
        print(f"{n} -  {count:x}H - {(word)} :linea correcta")
        return count + 1


def analizeCodeSegment(
    codeSegment, tuplaNombreVariables8bits, tuplaNombresVariables16bits, n, count
):
    print(f"{n+1} -  {count:x}H - code segment :linea correcta")
    count = count - count
    for n, line in enumerate(codeSegment, start=n + 2):
        if line.startswith(instrucciones_sin_operando):
            line = cleanLine(line)
            count = checkLinewithoutOperands(line, n, count)
        elif line.startswith(instrucciones_con_operandos):
            count = analyzeOperandsCodeSegments(
                line, tuplaNombreVariables8bits, tuplaNombresVariables16bits, n, count
            )

        elif line.startswith(instruccionconDosOperandos):
            analyzeTwoOperandsCodeSegments(
                line, tuplaNombreVariables8bits, tuplaNombresVariables16bits, n, count
            )
        elif line.startswith(instrucciones_con_un_operando):
            bool, count = analyzeOneOperandCodeSegments(
                line, tuplaNombreVariables8bits, tuplaNombresVariables16bits, n, count
            )
        elif line.startswith(instrucciondeSaltos):
            analyceJumps(
                line,
                n,
                labels,
                tuplaNombreVariables8bits,
                tuplaNombresVariables16bits,
                count,
            )

        elif line.startswith(OtrasInstrucciones):
            print(f"{n} -  {count:x}H - {line} :insturccion no asignada")
        elif line.startswith(numbers):
            print(f"{n} -  {count:x}H - {line} error: simbolo no definido")
        elif line.endswith(":"):
            if (CheckingEtiqueta(line)) == True:
                print(f"{n} -  {count:x}H - {line} : es una etiqueta")
                line = line.replace(":", "")
                hex_count = hex(count)[2:]
                result = line + " " + hex_count
                result = result.split(" ")
                labels.append(result)

            elif (CheckingEtiqueta(line)) == False:
                print(f"{n} -  {count:x}H - {line} : Error :parametros incorrectos")
        else:
            print(f"{n} -  {count:x}H - {line} es un error")
    print(f"{n+1} -  {count:x}H - ends :linea correcta")
    return count


while True:
    raw_file = open_file()
    clean_file = clear_File(raw_file)
    data_seccion = []
    stack_seccion = []
    code_seccion = []
    seccion_actual = None
    try:
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
    except Exception as e:
        print(e)

    variables8bits, variables16bits, n, count = AnalyzerDataSegment(data_seccion)

    variables8BitsN, variables16BitsN = CleanVariables(variables8bits, variables16bits)

    nombresVar8Bits = [variables8BitsN[0] for variables8BitsN in variables8BitsN]

    nombresVar16Bits = [variables16BitsN[0] for variables16BitsN in variables16BitsN]

    tuplaNombreVariables8bits = tuple(nombresVar8Bits)
    tuplaNombresVariables16bits = tuple(nombresVar16Bits)

    n, count = analyzeStackSegment(stack_seccion, n, count)

    count = analizeCodeSegment(
        code_seccion, tuplaNombreVariables8bits, tuplaNombresVariables16bits, n, count
    )

    tableVariables = variables8BitsN + variables16BitsN

    CreateTableVariables(tableVariables, labels)
    print("Presione ESC para salir")
    keyboard.wait("esc")
    break
