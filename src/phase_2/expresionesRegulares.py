import re
from tuples import *
from prettytable import PrettyTable


# expresion_regular = r'^(?P<nombre>[a-zA-Z_]\w*)\s+(?P<tipo>db|dw|EQU|equ)\s+(?P<valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-F]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-F]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))(\s+dup\s*\(\s*(?P<dup_valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-F]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-F]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))\s*\))?\s*$'

# expresion_regular = r'^(?P<nombre>[a-zA-Z_]\w*)\s+(?P<tipo>db|dw|EQU|equ)\s+(?P<valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-F]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-F]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))(\s+dup\s*\(\s*(?P<dup_valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-F]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-F]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))\s*\))?\s*$'
expresion_regular = r'^(?P<nombre>[a-zA-Z_]\w*)\s+(?P<tipo>db|dw|EQU|equ)\s+(?P<valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-Fa-f]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-Fa-f]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))(\s+dup\s*\(\s*(?P<dup_valor>(?:"(?:\\"|[^"])*"|\'(?:\\\'|[^\'])*\'|\b\d+[A-Fa-f]{0,1}H\b|\b\d+[Bb]{1}\b|-\b\d+[A-Fa-f]{0,1}H\b|-\b\d+[Bb]{1}\b|\b\d+|\b\d+[.]\d+))\s*\))?\s*$'
expresion_Nombrevariable = r"^\w+$"
expresionHexadecimal = r"^[0-9A-F]+H$"


def checkError(line, n):
    # esta funcion se encarga de verificar si la linea tiene errores de sintaxis
    # si tiene errores de sintaxis retorna False
    # si no tiene errores de sintaxis retorna True y se agrega la linea a la lista de variables
    if line.startswith(dbs):
        print(f"{n} - Error en la linea: {line} parametros incorrectos")
        return False
    elif line.startswith(equ):
        print(f"{n} - Error en la linea: {line} parametros incorrectos")
        return False

    # elif re.match(expresion_Nombrevariable, line):

    else:
        words = line.split(" ")
        if (len(words)) <= 2:
            print(f"{n} - {line} parametros insuficientes")
            return False

        else:
            if re.match(expresion_Nombrevariable, (words[0])):
                if words[1] in (dbs):
                    if re.match(expresionHexadecimal, (words[2])):
                        if len(words) == 3:
                            print(f"{n} - {line} :  correcto")
                            return True
                        elif len(words) <= 4:
                            if words[3] == "dup" or "DUP":
                                print(f"{n} - {line} :  correcto")
                                return True
                            else:
                                print(f"{n} - {line} : error parametros incorrectos")
                                return False

                elif words[1] in (equ):
                    pass
            else:
                print(f"{n} - {line} : nombre incorrecto en la variable ")
                return False


def AnalyzerDataSegment(sentences):
    # recorre las sentencias que es una lista de lineas del datasegement y busca el patron dado
    variables = []
    for n, cadena in enumerate(sentences, start=1):
        # buscar el patrón en la cadena
        coincidencia_patron = re.search((expresion_regular), cadena)

        if coincidencia_patron:
            ls = []
            ls.append(coincidencia_patron.group(1))
            ls.append(coincidencia_patron.group(2))
            ls.append(coincidencia_patron.group(2))
            ls.append(coincidencia_patron.group(3))
            variables.append(ls)
            print(f"{n} - {cadena} :   correcta")
        else:
            if (
                checkError(cadena, n) == True
            ):  # si la linea no tiene errores de sintaxis se agrega a la lista de variables
                variables.append(cadena)
            else:
                pass

    # Esta parte es para agregar el tipo y el tamaño de la variable
    for variable in variables:
        if variable[2] in dbs:
            variable[1] = "variable"
        elif variable[2] in equ:
            variable[1] = "constante"

    table = PrettyTable(["Simbolo", "Tipo", "Tamaño", "Valor"])

    # for list in variables:
    # table.add_row(list)

    # Falta por verificar que el valor de la variable sea correcto para cada tamaño de variable
    print(variables)
    return variables, n


def AnalyzeStackSegment(stack):
    # en este trozo se analñizara la sintaxis correcta de la pila
    pass
