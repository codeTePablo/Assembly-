from tuples import *
from dicts import *
from anlisisVariables import *
from prettytable import PrettyTable
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk

tuplasEqu = ["equ", "EQU"]

def CleanVariables(variables8bits, variables16bits):
    variables8Bits = []
    variables16Bits = []

    lista_sin_duplicados8bits = list(set(map(tuple, variables8bits)))
    lista_sin_duplicados16bits = list(set(map(tuple, variables16bits)))

    for elemento in variables8bits:
        if elemento not in variables8Bits:
            variables8Bits.append(elemento)
    for elemento in variables16bits:
        if elemento not in variables16Bits:
            variables16Bits.append(elemento)

    memoria8bits = new_list_for_memory(lista_sin_duplicados8bits)
    memoria16bits = new_list_for_memory(lista_sin_duplicados16bits)

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

    tuplaNombreVariables8bits = tuple(valores_modificados8bits)
    tuplaNombresVariables16bits = tuple(valores_modificados16bits)

    return tuplaNombreVariables8bits, tuplaNombresVariables16bits

def getDirecciones(variables8bits, variables16bits):
    
   
    
    direccionVariables8bits = []
    direccionVariables16bits = []

    for variable in variables8bits:
        print (variable)
        direccionVariables8bits.append (variable[-1:])
    for variable in variables16bits:
        print (variable)
        direccionVariables16bits.append (variable[-1:])

    

    print (direccionVariables8bits)
    print (direccionVariables16bits)



    return direccionVariables8bits, direccionVariables16bits


def CreateTableVariables(tableVariables, labels):
    for sublista in tableVariables:
        if len(sublista) == 5:
            valor = " ".join(sublista[2:4])
            del sublista[2:4]
            sublista.insert(2, valor)

    for sublista in tableVariables:
        if sublista[1] in dbs:
            sublista.insert(1, "variable")
        elif sublista[1] in equ:
            sublista.insert(1, "constante")

    for sublista in tableVariables:
        if sublista[2] in equ:
            sublista[2] = "dw"

    for label in labels:
        label.append("etiqueta")
        label.append("Null")
        label.append("Null")

        label.append(label[1] + "H")
        label.pop(1)

    tableVariables = tableVariables + labels
    print("Tabla de simbolos:")

    table = PrettyTable(["Simbolo", "Tipo", "Tamaño", "Valor", "Direccion"])

    for list in tableVariables:
        table.add_row(list)

    print(table)


def new_list_for_memory(line):
    new_list = [[x[0]] for x in line]
    return new_list


def cleanLine(line):
    line = line.replace(",", " ").rstrip().lstrip()
    line = line.replace("  ", "").rstrip().lstrip()
    return line


def analyzeStackSegment(stackSegment, n, count):
    n = 1 + n
    print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - stack segment - linea correcta")
    count = count - count
    for n, line in enumerate(stackSegment, start=n + 1):
        line = cleanLine(line)
        line = line.split(" ")
        if len(line) == 3:
            decimal = convertir_a_decimal(line[1])
            if decimal <= 65535 and decimal >= -32768:
                patron = r"dup\((.+?)\)"  # el patrón busca la palabra "dup" seguida de paréntesis y uno o más dígitos dentro
                resultado = re.search(patron, line[2])
                if resultado:
                    numero = convertir_a_decimal(resultado.group(1))
                    if numero <= 65535 and numero >= -32768:
                        print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {' '.join(line)} - linea correcta")
                        # se le suma algo xd

                        count = decimal * 2
                    else:
                        print(
                            f"{n} -  {format(count, 'x').zfill(4).upper()}H - {' '.join(line)} Error: el valor  excede el rango de 16 bits"
                        )
                        # no se le suma nada
                else:
                    print(
                        f"{n} -  {format(count, 'x').zfill(4).upper()}H - {' '.join(line)} Error: la sintaxis de la linea es incorrecta"
                    )
                    # No se le suma nada
            else:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H - {' '.join(line)} Error: el valor  excede el rango de 16 bits"
                )

        else:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: la sintaxis de la linea es incorrecta"
            )

    n = n + 1
    print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - ends :linea correcta")
    return n, count


def CheckingEtiqueta(etiqueta, count, n, line):
    patron = r"^(?P<etiqueta>[a-zA-Z_]\w*\s*):$"
    coincidencias = re.search((patron), etiqueta)
    if coincidencias:
        print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} : etiqueta correcta")
        
        return True
    else:
        print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} : Error en la etiqueta")
        return False


def getSections(clean_file):
    data_section = []
    stack_section = []
    code_section = []
    section_actual = None
    try:
        for linea in clean_file:
            if "data segment" in linea:
                section_actual = data_section
            elif "stack segment" in linea:
                section_actual = stack_section
            elif "code segment" in linea:
                section_actual = code_section
            elif "ends" in linea:
                section_actual = None
            elif section_actual is not None:
                section_actual.append(linea)
    except Exception as e:
        print(e)

    return data_section, stack_section, code_section


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
