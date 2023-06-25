from tuples import (
    registros16bits,
    registros8bits,
)
from anlisisVariables import *


def cleanLine(line):
    line = line.replace(",", " ").rstrip().lstrip()
    line = line.replace("  ", " ")
    return line


# def analyzeOperandsCodeSegments(linea, tupla Variables):


def analyzeOperandsCodeSegments(
    linea, tuplaNombreVariables8bits, tuplaNombresVariables16bits, n
):
    linea = cleanLine(linea)
    componentes = linea.split()
    parametros = componentes[1:]

    if len(parametros) == 2:
        param1 = parametros[0].lower()
        param2 = parametros[1]

        if param1 in registros16bits and param2 in tuplaNombresVariables16bits:
            print("Linea correcta")
            return True
        elif param1 in tuplaNombresVariables16bits and param2 in registros16bits:
            print("Linea correcta")
            return True
        elif param1 in registros8bits and param2 in tuplaNombreVariables8bits:
            print("Linea correcta")
            return True
        elif param1 in tuplaNombreVariables8bits and param2 in registros8bits:
            print("Linea correcta")
            return True
        elif param1 in registros16bits and param2 in registros8bits:
            print("Error: No se puede operar un registro de 16 bits con uno de 8 bits")
            return False
        elif param1 in registros8bits and param2 in registros16bits:
            print("Error: No se puede operar un registro de 8 bits con uno de 16 bits")
            return False
        elif param1 in registros16bits and param2 in tuplaNombreVariables8bits:
            print(
                "Error: No se puede operar un registro de 16 bits con variables de 8 bits"
            )
            return False
        elif param1 in tuplaNombreVariables8bits and param2 in registros16bits:
            print(
                "Error: No se puede operar variables de 8 bits con un registro de 16 bits"
            )
            return False
        elif (
            param1 in tuplaNombreVariables8bits
            and param2 in tuplaNombresVariables16bits
        ):
            print(
                "Error: No se puede operar variables de 8 bits con variables de 16 bits"
            )
            return False
        elif param1 in registros8bits:
            inmediato = convertir_a_decimal(param2)
            if inmediato <= 255 and inmediato >= -128:
                return True
            else:
                print(f"{n} - {linea} Error: El parametro {param2} excede los 8 bits")
        elif param1 in registros16bits:
            inmediato = convertir_a_decimal(param2)
            if inmediato <= 65535 and inmediato >= -32768:
                return True
            else:
                print(f"{n} - {linea} Error: El parametro {param2} excede los 16 bits")

        elif param1 in tuplaNombreVariables8bits:
            inmediato = convertir_a_decimal(param2)
            if inmediato <= 255 and inmediato >= -128:
                return True
            else:
                print(f"{n} - {linea} Error: El parametro {param2} excede los 8 bits")
        elif param1 in tuplaNombresVariables16bits:
            inmediato = convertir_a_decimal(param2)
            if inmediato <= 65535 and inmediato >= -32768:
                return True
            else:
                print(f"{n} - {linea} Error: El parametro {param2} excede los 16 bits")
        else:
            print(f"{n} - {linea} Error: No se reconoce los parametros")

    else:
        print(f"{n} - {linea} {componentes} Error: Argumentos invalidos")


def analyzeTwoOperandsCodeSegments(
    line, tuplaNombreVariables8bits, tuplaNombresVariables16bits, n
):
    line = cleanLine(line)
    componentes = line.split()
    parametros = componentes[1:]

    if len(parametros) == 2:
        if (
            parametros[0] in registros16bits
            and parametros[1] in tuplaNombresVariables16bits
        ):
            print(f"{n} - {line}: Linea correcta")
            return True
        elif (
            parametros[0] in registros8bits
            and parametros[1] in tuplaNombreVariables8bits
        ):
            print(f"{n} - {line}: Linea correcta")
            return True
        elif (
            parametros[0] in registros16bits
            and parametros[1] in tuplaNombreVariables8bits
        ):
            print(
                f"{n} - {line}: Linea incorrecta no se puede operar 16 bits con 8 bits"
            )
            return True
        elif (
            parametros[0] in registros8bits
            and parametros[1] in tuplaNombresVariables16bits
        ):
            print(
                f"{n} - {line}: Linea incorrecta no se puede operar 8 bits con 16 bits"
            )
            return True

        elif parametros[0] in tuplaNombresVariables16bits:
            print(
                f"{n} - {line}: Error: no es posible usar variabele y registros en ese orden "
            )
            return False

        elif parametros[0] in tuplaNombreVariables8bits:
            print(
                f"{n} - {line}: Error: no es posible usar variabele y registros en ese orden "
            )
        else:
            print(f"{n} - {line} Correcto")
    else:
        print(f"{n} - {line} Error: Argumentos invalidos")


etiquetasmodificadas = []


def analyceJumps(
    line, n, etiquetas, tuplaNombreVariables8bits, tuplaNombresVariables16bits
):
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
        if parametros[0] in tuplaNombreVariables8bits:
            print(f"{n} - {line} Error: No se puede saltar a una variable")
        elif parametros[0] in tuplaNombresVariables16bits:
            print(f"{n} - {line} Error: No se puede saltar a una variable")
        elif parametros[0] in tuplaEtiquetas:
            print(f"{n} - {line} Salto de linea valido")
        else:
            print(f"{n} - {line} Error: Etiqueta no encontrada")
    if len(parametros) > 1:
        print(f"{n} - {line} Error: Esta instruccion solo debe tener un operando")


def analyzeOneOperandCodeSegments(
    line, tuplaNombreVariables8bits, tuplaNombreVariables16bits, n
):
    tuplaNombreVariables8bits = tuple(
        elemento.upper() if isinstance(elemento, str) else elemento
        for elemento in tuplaNombreVariables8bits
    )
    tuplaNombreVariables16bits = tuple(
        elemento.upper() if isinstance(elemento, str) else elemento
        for elemento in tuplaNombreVariables16bits
    )

    line = cleanLine(line)
    componentes = line.split()

    parametros = componentes[1:]

    if len(parametros) == 1:
        if parametros[0] in registros16bits:
            print(f"{n} - {line} Linea correcta")
            return True
        elif parametros[0] in registros8bits:
            print(f"{n} - {line} Linea correcta")
            return True
        elif parametros[0] in tuplaNombreVariables8bits:
            print(f"{n} - {line} Linea correcta")
            return True
        elif parametros[0] in tuplaNombreVariables16bits:
            print(f"{n} - {line} Linea correcta")
            return True
        else:
            print(f"{n} - {line} variable no encontrada")
            return False
    else:
        print(f"{n} - {line} Error: Instruction solo debe llevar un operando")
