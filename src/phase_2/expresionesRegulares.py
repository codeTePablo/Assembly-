import re
from tuples import *
from prettytable import PrettyTable


# = r'^(?P<nombre>[a-zA-Z_]\w*)\s+(?P<tipo>db|dw|EQU|equ|DB|DW)\s+(?P<valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\')|-?\d+(?P<dup>\s*(DUP|dup)\s*\(\s*\d+\s*\))?)$'
# expresion_regular = r'^(?P<nombre>[a-zA-Z_]\w*)\s+(?P<tipo>db|dw|EQU|equ)\s+(?P<valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-F]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-F]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))(\s+dup\s*\(\s*(?P<dup_valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-F]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-F]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))\s*\))?\s*$'

# expresion_regular = r'^(?P<nombre>[a-zA-Z_]\w*)\s+(?P<tipo>db|dw|EQU|equ)\s+(?P<valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-F]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-F]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))(\s+dup\s*\(\s*(?P<dup_valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-F]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-F]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))\s*\))?\s*$'
expresion_regular = r'^(?P<nombre>[a-zA-Z_]\w*)\s+(?P<tipo>db|dw|EQU|equ)\s+(?P<valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-Fa-f]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-Fa-f]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))(\s+dup\s*\(\s*(?P<dup_valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-Fa-f]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-Fa-f]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))\s*\))?\s*$'


def AnalyzerDataSegment(sentences):
    variables = []
    for cadena in sentences:
        # buscar el patrón en la cadena
        coincidencia_patron = re.search((expresion_regular), cadena)

        if coincidencia_patron:
            ls = []
            ls.append(coincidencia_patron.group(1))
            ls.append(coincidencia_patron.group(2))
            ls.append(coincidencia_patron.group(2))
            ls.append(coincidencia_patron.group(3))
            variables.append(ls)
        else:
            print("Error en la linea: " + cadena + " linea no valida")

    for variable in variables:
        if variable[2] in dbs:
            variable[1] = "variable"
        elif variable[2] in equ:
            variable[1] = "constante"

    table = PrettyTable(["Simbolo", "Tipo", "Tamaño", "Valor"])

    for list in variables:
        table.add_row(list)

    print(table)


def AnalyzeStackSegment(stack):
    patron = r"^dw\s+(\d{1,5})\s+(dup|DUP)\s?\(\s*(-?\d{1,5}|[0-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-3]\d|6553[0-5])\s*\)$"
    coincidencia_patron = re.search((patron), stack)
    if coincidencia_patron:
        print("Tamaño de la pila: " + coincidencia_patron.group(1))
        print("Valor de la pila: " + coincidencia_patron.group(3))
    else:
        print("Error en la linea: " + stack + " linea no valida")
