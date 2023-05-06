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
                            print(f"{n} - {line} :   correcto")
                            return True
                        elif len(words) <= 4:
                            if words[3] == "dup" or "DUP":
                                print(f"{n} - {line} :   correcto")
                                return True
                            else:
                                print(f"{n} - {line} : error parametros incorrectos")
                                return False

                elif words[1] in (equ):
                    pass
            else:
                print(f"{n} - {line} : nombre incorrecto en la variable ")
                return False


def convertir_bits(tupla):
    """Esta funcion se encarga de convertir los valores de las variables a 8 y 16 bits si hay valores bianrios o hexadecimales"""
    resultado = []
    for elemento in tupla:
        if elemento.endswith("B"):
            decimal = int(elemento[:-1], 2)
            resultado.append(decimal)
        elif elemento.endswith("H"):
            decimal = int(elemento[:-1], 16)
            resultado.append(decimal)
        else:
            resultado.append(elemento)
    # print(resultado)
    return tuple(resultado)


def sin_strings(lista):
    """Esta funcion se encarga de verificar si la lista tiene strings y los elimina"""
    # lista = ["10101010B", "Hola", "0F800H", "50"]
    nueva_lista = []

    for valor in lista:
        if isinstance(valor, str):
            if valor.endswith("B"):
                try:
                    nueva_lista.append(valor)
                except ValueError:
                    pass
            elif valor.endswith("H"):
                try:
                    nueva_lista.append(valor)
                except ValueError:
                    pass
            else:
                try:
                    int(valor)
                    nueva_lista.append(valor)
                except ValueError:
                    pass
        else:
            # pass
            nueva_lista.append(valor)
    # print(nueva_lista)
    return nueva_lista


def AnalyzerDataSegment(sentences):
    # print(sentences)
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
            print(f"{n} - {cadena} :   correcto")
        else:
            if checkError(cadena, n) == True:
                words = cadena.split(" ")
                tamaño = len(words)
                if tamaño == 3:
                    words.append(words[2])
                    if words[1] in dbs:
                        words[1] = "variable"
                        words[2] = "db"
                        variables.append(words)
                    elif words[1] in equ:
                        words[1] = "constante"
                        words[2] = "equ"
                        variables.append(words)
                elif tamaño >= 4:
                    if words[1] == "db" or "DB":
                        words[1] = "variable"
                        words[2] = "db"
                        variables.append(words)
                    elif words[1] == "dw" or "DW":
                        words[1] = "variable"
                        words[2] = "dw"
                        variables.append(words)
                    elif words[1] in equ:
                        words[1] = "constante"
                        words[2] = "equ"
                        variables.append(words)
            else:
                pass

    # Esta parte es para agregar el tipo y el tamaño de la variable
    new_list_valor_8bits = []  # lista para guardar los valores de las variables
    new_list_valor_16bits = []  # lista para guardar los valores de las variables

    for variable in variables:
        if variable[2] == "db":
            valor = variable[3]
            try:
                if valor[-1] == "B":
                    # Convertir valor binario a decimal
                    decimal_valor = int(valor[:-1], 2)
                elif valor[-1] == "H":
                    # Convertir valor hexadecimal a decimal
                    decimal_valor = int(valor[:-1], 16)
                else:
                    # Convertir valor decimal a entero
                    decimal_valor = int(valor)

                if decimal_valor > 255:
                    print(
                        f"Error en {variable} - el valor de db no puede sobrepasar de 255"
                    )
                else:
                    new_list_valor_8bits.append(decimal_valor)
            except ValueError:
                # print(f"palabra")
                pass

        if variable[2] == "dw":
            valor = variable[3]
            try:
                if valor[-1] == "B":
                    # Convertir valor binario a decimal
                    decimal_valor = int(valor[:-1], 2)
                elif valor[-1] == "H":
                    # Convertir valor hexadecimal a decimal
                    decimal_valor = int(valor[:-1], 16)
                else:
                    # Convertir valor decimal a entero
                    decimal_valor = int(valor)

                if decimal_valor > 65535:
                    print(
                        f"Error en {variable} - el valor de dw no puede sobrepasar de 65535"
                    )
                else:
                    new_list_valor_16bits.append(decimal_valor)
            except ValueError:
                # print(f"palabra")
                pass

    # eliminar los strings de las listas
    print(new_list_valor_8bits)
    print(new_list_valor_16bits)

    table = PrettyTable(["Simbolo", "Tipo", "Tamaño", "Valor"])

    for list in variables:
        table.add_row(list)
    print(variables)
    print(table)

    # Falta por verificar que el valor de la variable sea correcto para cada tamaño de variable
    return variables, n


def CheckingEtiqueta(etiqueta):
    patron = r"^(?P<etiqueta>[a-zA-Z_]\w*\s*):$"
    coincidencias = re.search((patron), etiqueta)
    if coincidencias:
        return True
    else:
        return False


def AnalyzeStackSegment(stack):
    # en este trozo se analñizara la sintaxis correcta de la pila
    pass


if __name__ == "__main__":
    sin_strings()
