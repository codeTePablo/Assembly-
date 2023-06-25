import re

variablesCorrectas = []

tuplasdw = ["dw", "DW", "EQU", "equ"]
tuplasdb = ["db", "DB"]
variables16bits = []
variables8bits = []


def convertir_a_decimal(string):
    if string.endswith("B") or string.endswith("b"):
        binario = string[:-1]
        decimal = int(binario, 2)
        return decimal
    elif string.endswith("H") or string.endswith("h"):
        hexadecimal = string[:-1]
        decimal = int(hexadecimal, 16)
        return decimal
    else:
        try:
            decimal = int(string)
            return decimal
        except ValueError:
            return "Error: el string contiene caracteres no numéricos"


def convertir_a_decimalS(string):
    if string.endswith("B") or string.endswith("b"):
        binario = string[:-1]
        decimal = int(binario, 2)
        return decimal
    elif string.endswith("H") or string.endswith("h"):
        hexadecimal = string[:-1]
        decimal = int(hexadecimal, 16)
        return decimal
    else:
        try:
            decimal = int(string)
            return decimal
        except ValueError:
            return string


def cleanLine(line):
    line = line.replace(",", " ").rstrip().lstrip()
    return line


def checkType(lineClean, n):
    # Si la linea tiene 3 parametros
    if len(lineClean) == 3:
        # Si el segundo parametro es db
        if lineClean[1] in tuplasdb:
            if lineClean[2].endswith("h") or lineClean[2].endswith("H"):
                # si es hexadcimal en db
                hexadecimal = lineClean[2][:-1]
                decimal = int(hexadecimal, 16)
                if decimal <= 255 and decimal >= -128:
                    variables8bits.append(lineClean)
                    print(f"{n} - {' '.join(lineClean)} : linea Correcta")
                    return lineClean

                else:
                    print(
                        f"{n} - {' '.join(lineClean)} : linea Incorrecta, el valor hexadecimal excede el rango de 8 bits"
                    )
                    return ""
            elif lineClean[2].endswith("b") or lineClean[2].endswith("B"):
                binario = lineClean[2][:-1]
                decimal = int(binario, 2)
                if decimal <= 255 and decimal >= -128:
                    variables8bits.append(lineClean)
                    print(f"{n} - {' '.join(lineClean)} : linea Correcta")
                    return lineClean

                else:
                    print(
                        f"{n} - {' '.join(lineClean)} : linea Incorrecta, el valor binario excede el rango de 8 bits"
                    )
                    return ""

            elif lineClean[2].isdigit():
                decimal = int(lineClean[2])
                if decimal <= 255 and decimal >= -128:
                    variables8bits.append(lineClean)
                    print(f"{n} - {' '.join(lineClean)} : linea Correcta")
                    return lineClean

                else:
                    print(
                        f"{n} - {' '.join(lineClean)} : linea Incorrecta, el valor decimal excede el rango de 8 bits"
                    )
                    return ""
            # Si el valor es un caracter
            else:
                variables8bits.append(lineClean)
                print(f"{n} - {' '.join(lineClean)} : linea correcta")
                return lineClean

        # Si el segundo parametro es dw
        elif lineClean[1] in tuplasdw:
            if lineClean[2].endswith("h") or lineClean[2].endswith("H"):
                hexadecimal = lineClean[2][:-1]
                decimal = int(hexadecimal, 16)
                if decimal <= 65535 and decimal >= -32769:
                    variables16bits.append(lineClean)
                    print(f"{n} - {' '.join(lineClean)} : linea Correcta")
                    return lineClean
                else:
                    print(
                        f"{n} - {' '.join(lineClean)} : linea Incorrecta, el valor hexadecimal excede el rango de 16 bits"
                    )
                    return ""
            elif lineClean[2].endswith("b") or lineClean[2].endswith("B"):
                binario = lineClean[2][:-1]
                decimal = int(binario, 2)
                if decimal <= 65535 and decimal >= -32769:
                    variables16bits.append(lineClean)

                    print(f"{n} - {' '.join(lineClean)} : linea Correcta")
                    return lineClean
                else:
                    print(
                        f"{n} - {' '.join(lineClean)} : linea Incorrecta, el valor binario excede el rango de 16 bits"
                    )
                    return ""
            elif lineClean[2].isdigit():
                decimal = int(lineClean[2])
                if decimal <= 65535 and decimal >= -32769:
                    variables16bits.append(lineClean)
                    print(f"{n} - {' '.join(lineClean)} : linea Correcta")
                    return lineClean
                else:
                    print(
                        f"{n} - {' '.join(lineClean)} : linea Incorrecta, el valor decimal excede el rango de 16 bits"
                    )
                    return ""
            else:
                variables16bits.append(lineClean)
                print(f"{n} - {' '.join(lineClean)} : linea correcta")
                return lineClean

    # Si la linea tiene 4 parametros
    elif len(lineClean) == 4:
        if lineClean[1] in tuplasdb:
            decimal = convertir_a_decimal(lineClean[2])
            if decimal <= 65535 and decimal >= -32769:
                patron = r"dup\((.+?)\)"  # el patrón busca la palabra "dup" seguida de paréntesis y uno o más dígitos dentro
                resultado = re.search(patron, lineClean[3])
                if resultado:  # si se encontró un resultado
                    numero = resultado.group(1)
                    if numero.startswith("'") or numero.startswith('"'):
                        print(f"{n} - {' '.join(lineClean)} : linea correcta")
                        return lineClean
                    else:
                        decimal = convertir_a_decimal(numero)
                        if decimal <= 255 and decimal >= -128:
                            print(f"{n} - {' '.join(lineClean)} : linea correcta")
                            return lineClean
                        else:
                            print(
                                f"{n} - {' '.join(lineClean)} : linea Incorrecta, el valor decimal excede el rango de 8 bits"
                            )
                            return ""

            else:
                print(f"Error: el valor {lineClean} excede el rango de 16 bits")
        elif lineClean[1] in tuplasdw:
            decimal = convertir_a_decimal(lineClean[2])
            if decimal <= 65535 and decimal >= -32769:
                patron = r"dup\((.+?)\)"  # el patrón busca la palabra "dup" seguida de paréntesis y uno o más dígitos dentro
                resultado = re.search(patron, lineClean[3])
                if resultado:  # si se encontró un resultado
                    numero = resultado.group(1)
                    if numero.startswith("'") or numero.startswith('"'):
                        print(f"{n} - {' '.join(lineClean)} : linea correcta")
                        return lineClean
                    else:
                        decimal = convertir_a_decimal(numero)
                        if decimal <= 65535 and decimal >= -32769:
                            print(f"{n} - {' '.join(lineClean)} : linea correcta")
                            return lineClean
                        else:
                            print(
                                f"{n} - {' '.join(lineClean)} : linea Incorrecta, el valor {numero}  excede el rango de 16 bits"
                            )
                            return ""
                else:
                    print(f"Error: el valor {lineClean} excede el rango de 16 bits")
            else:
                print(f"Error: el valor {lineClean} excede el rango de 16 bits")


def AnalyzerDataSegment(dataSegment):
    count = 0
    n=0
    print(f"1 - {hex(count)}- data segment : correcto")
    for n, line in enumerate(dataSegment, start=2):
        lineClean = cleanLine(line)
        lineClean = lineClean.split(" ")

        if len(lineClean) <= 2:
            word = "".join(line).rstrip().lstrip()
            print(f"{n} - {word} :error :linea con parametros insuficientes")
        else:
            if len(lineClean[0]) > 10:
                print(
                    f"{n}- {lineClean[0]} :error : nombre de variable excede los 10 caracteres"
                )
            else:
                line816 = checkType(lineClean, n)

                if line816 == "":
                    pass
                elif line816 == None:
                    pass
                else:
                    if line816[1] in tuplasdb:
                        variables8bits.append(line816)
                    elif line816[1] in tuplasdw:
                        variables16bits.append(line816)

    n = n + 1
    print(f"{n} - ends : correcto")
    return variables8bits, variables16bits, n
