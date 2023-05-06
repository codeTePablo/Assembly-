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
            return True
        elif parametros[0] in tuplaVariables16bits and parametros[1] in registros16bits:
            return True
        elif parametros[0] in registros16bits and parametros[1] in registros16bits:
            return True
        elif parametros[0] in registros8bits and parametros[1] in variables8bits:
            return True
        elif parametros[0] in variables8bits and parametros[1] in registros8bits:
            return True
        elif parametros[0] in registros8bits and parametros[1] in registros8bits:
            return True
        elif parametros[0] in variables8bits and parametros[1] in variables8bits:
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
            print(f"{n} - {linea} Error: Operando no valido")


def analyzeTwoOperandsCodeSegments(line, tuplaVariables8bits, tuplaVariables16bits, n):
    line = cleanLine(line)
    componentes = line.split()
    parametros = componentes[1:]

    if len(parametros) != 2:
        print(f"{n} - {line} Error: Esta instruccion debe tener 2 operandos")
    else:
        if parametros[0] in registros16bits and parametros[1] in tuplaVariables16bits:
            print(f"{n} - {line}: Linea correcta")
            return True
        elif parametros[0] in registros8bits and parametros[1] in tuplaVariables8bits:
            print(f"{n} - {line}: Linea correcta")
            return True
        elif parametros[0] in registros16bits and parametros[1] in tuplaVariables8bits:
            print(
                f"{n} - {line}: Linea incorrecta no se puede operar 16 bits con 8 bits"
            )
            return True
        elif parametros[0] in registros8bits and parametros[1] in tuplaVariables16bits:
            print(
                f"{n} - {line}: Linea incorrecta no se puede operar 8 bits con 16 bits"
            )
            return True

        elif parametros[0] in tuplaVariables16bits:
            print(
                f"{n} - {line}: Error: no es posible usar variabele y registros en ese orden "
            )
            return False

        elif parametros[0] in tuplaVariables8bits:
            print(
                f"{n} - {line}: Error: no es posible usar variabele y registros en ese orden "
            )


etiquetasmodificadas = []


def analyceJumps(line, n, etiquetas, tuplaVariables8bits, tuplaVariables16bits):
    line = cleanLine(line)

    for elemento in etiquetas:
        valor = elemento[0]
        valor = valor.replace("[", "").replace("]", "")
        valor = valor.replace("'", "")
        valor = valor.upper()

        etiquetasmodificadas.append(valor)

    tuplaEtiquetas = tuple(etiquetasmodificadas)

    componentes = line.split()
    parametros = componentes[1:]

    if len(parametros) == 0:
        print(f"{n} - {line} Salto de linea valido")
    elif len(parametros) == 1:
        if parametros[0] in tuplaVariables8bits:
            print(f"{n} - {line} Error: No se puede saltar a una variable")
        elif parametros[0] in tuplaVariables16bits:
            print(f"{n} - {line} Error: No se puede saltar a una variable")
        elif parametros[0] in tuplaEtiquetas:
            print(f"{n} - {line} Salto de linea valido")
        else:
            print(f"{n} - {line} Error: Etiqueta no encontrada")
    if len(parametros) > 1:
        print(f"{n} - {line} Error: Esta instruccion solo debe tener un operando")


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
