from tuples import *
from dicts import *
from prettytable import PrettyTable


def CleanVariables(variables8bits, variables16bits):
    variables8Bits = []
    variables16Bits = []
    for elemento in variables8bits:
        if elemento not in variables8Bits:
            variables8Bits.append(elemento)
    for elemento in variables16bits:
        if elemento not in variables16Bits:
            variables16Bits.append(elemento)

    memoria8bits = new_list_for_memory(variables8Bits)
    memoria16bits = new_list_for_memory(variables16bits)

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

    return variables8Bits, variables16Bits


def CreateTableVariables(tableVariables, labels):
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


def new_list_for_memory(line):
    new_list = [[x[0]] for x in line]
    # print(f"la nueva lista: {new_list}")
    return new_list


def analyzeStackSegment(stackSegment, n):
    n = 1 + n
    print(f"{n} - stack segment - linea correcta")
    for n, line in enumerate(stackSegment, start=n + 1):
        print(f"{n} - {line} :linea correcta")
    n = n + 1
    print(f"{n} - ends :linea correcta")
    return n
