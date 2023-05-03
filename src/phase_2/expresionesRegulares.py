import re
from tuples import *
from prettytable import PrettyTable


# expresion_regular = r'^(?P<nombre>[a-zA-Z_]\w*)\s+(?P<tipo>db|dw|EQU|equ)\s+(?P<valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-F]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-F]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))(\s+dup\s*\(\s*(?P<dup_valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-F]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-F]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))\s*\))?\s*$'

# expresion_regular = r'^(?P<nombre>[a-zA-Z_]\w*)\s+(?P<tipo>db|dw|EQU|equ)\s+(?P<valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-F]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-F]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))(\s+dup\s*\(\s*(?P<dup_valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-F]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-F]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))\s*\))?\s*$'
expresion_regular = r'^(?P<nombre>[a-zA-Z_]\w*)\s+(?P<tipo>db|dw|EQU|equ)\s+(?P<valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-Fa-f]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-Fa-f]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))(\s+dup\s*\(\s*(?P<dup_valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-Fa-f]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-Fa-f]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))\s*\))?\s*$'


def AnalyzerDataSegment(sentences):
    # recorre las sentencias que es una lista de lineas del datasegement y busca el patron dado
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
    # en este trozo se analñizara la sintaxis correcta de la pila
    pass
