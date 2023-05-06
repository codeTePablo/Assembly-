from tuples import (
    registros16bits,
    registros8bits,
)
from anlisisVariables import convertir_a_decimal


def cleanLine(line):
    line = line.replace(",", " ").rstrip().lstrip()
    line = line.replace("  ", " ")
    return line


# def analyzeOperandsCodeSegments(linea, tupla Variables):


def analyzeOperandsCodeSegments(linea, variables8bits, tuplaVariables16bits, n):
    linea = cleanLine(linea)
    componentes = linea.split()
    parametros = componentes[1:]
    if len(parametros) != 2:  # Si no hay 2 parametros
        return False
    else:
        if parametros[0] in registros16bits and parametros[1] in tuplaVariables16bits:
            print("1")
            return True
        elif parametros[0] in tuplaVariables16bits and parametros[1] in registros16bits:
            print("2")
            return True
        elif parametros[0] in registros16bits and parametros[1] in registros16bits:
            print("3")
            return True
        elif parametros[0] in registros8bits and parametros[1] in variables8bits:
            print("4")
            return True
        elif parametros[0] in variables8bits and parametros[1] in registros8bits:
            print("5")
            return True
        elif parametros[0] in registros8bits and parametros[1] in registros8bits:
            print("6")
            return True
        elif parametros[0] in variables8bits and parametros[1] in variables8bits:
            print("7")
            return True
        elif parametros[0] in registros16bits and parametros[1] in registros8bits:
            print("Error: No se puede operar un registro de 16 bits con uno de 8 bits")
            return False
        elif parametros[0] in registros8bits and parametros[1] in registros16bits:
            print("Error: No se puede operar un registro de 8 bits con uno de 16 bits")
            return False
        elif parametros[0] in registros16bits and parametros[1] in variables8bits:
            print(
                "Error: No se puede operar un registro de 16 bits con variables de 8 bits"
            )
            return False
        elif parametros[0] in variables8bits and parametros[1] in registros16bits:
            print(
                "Error: No se puede operar variables de 8 bits con un registro  de 16 bits"
            )
            return False
        elif parametros[0] in variables8bits and parametros[1] in tuplaVariables16bits:
            print
            ("Error: No se puede operar variables de 8 bits con variables de 16 bits")
            return False
        else:
            pass


def analyzeoneOperandCodeSegments(line, tuplavariables8bits, tuplaVariables16bits, n):
    line = cleanLine(line)
    componentes = line.split()

    parametros = componentes[1:]

    if len(parametros) > 1:
        print(f"{n} - {line}  Error: Esta instruccion solo debe tener un operando")
    if len(parametros) == 1:
        if parametros[0] in registros16bits:
            return True
        elif parametros[0] in registros8bits:
            return True
        elif parametros[0] in tuplavariables8bits:
            return True
        elif parametros[0] in tuplaVariables16bits:
            return True
        else:
            print(f"{n} - {line} variable no encontrada")
            return False
