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
    linea, tuplaNombreVariables8bits, tuplaNombresVariables16bits, n, count
):
    # Esta funcion analiza las lineas que tienen dos operandos del orden
    # REG, memory
    # memory, REG
    # REG, REG
    # memory, immediate
    # REG, immediate

    line = cleanLine(linea)
    componentes = line.split()
    # print(componentes)
    parametro = componentes[1:]

    if len(parametro) == 2:
        param1 = parametro[0]
        param2 = parametro[1]

        if param1 in registros16bits and param2 in tuplaNombresVariables16bits:
            print(f"{n} -   {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta")
            return count + 4
        elif param1 in tuplaNombresVariables16bits and param2 in registros16bits:
            print(f"{n} -   {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta")
            return count + 4
        elif param1 in registros8bits and param2 in tuplaNombreVariables8bits:
            print(f"{n} -   {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta")
            return count + 3
        elif param1 in tuplaNombreVariables8bits and param2 in registros8bits:
            print(f"{n} -   {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta")
            return count + 3
        elif param1 in registros16bits and param2 in registros16bits:
            print(f"{n} -   {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta")
            return count + 2
        elif param1 in registros8bits and param2 in registros8bits:
            print(f"{n} -   {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta")
            return count + 2
        elif param1 in registros16bits and param2 in registros8bits:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: No se puede operar un registro de 16 bits con uno de 8 bits"
            )
            return count
        elif param1 in registros8bits and param2 in registros16bits:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: No se puede operar un registro de 8 bits con uno de 16 bits"
            )
            return count
        elif param1 in registros16bits and param2 in tuplaNombreVariables8bits:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: No se puede operar un registro de 16 bits con variables de 8 bits"
            )
            return count
        elif param1 in tuplaNombreVariables8bits and param2 in registros16bits:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: No se puede operar variables de 8 bits con un registro de 16 bits"
            )
            return count
        elif (
            param1 in tuplaNombreVariables8bits
            and param2 in tuplaNombresVariables16bits
        ):
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: No se puede operar variables de 8 bits con variables de 16 bits"
            )
            return count
        elif param1 in registros8bits:
            inmediato = convertir_a_decimal(param2)
            if inmediato <= 255 and inmediato >= -128:
                print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta")
                return count + 3
            else:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H - {linea} Error: El parametro {param2} excede los 8 bits"
                )
        elif param1 in registros16bits:
            if inmediato > 255 and inmediato < -128:
                print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta")
                return count + 3
            elif inmediato <= 65535 and inmediato >= -32768:
                print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta")
                return count + 4
            else:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H -{linea} Error: El parametro {param2} excede los 16 bits"
                )

        elif param1 in tuplaNombreVariables8bits:
            inmediato = convertir_a_decimal(param2)
            if inmediato <= 255 and inmediato >= -128:
                print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta")
                return count + 1
            else:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H  - {linea} Error: El parametro {param2} excede los 8 bits"
                )
        elif param1 in tuplaNombresVariables16bits:
            if inmediato > 255 and inmediato < -128:
                print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta")
                return count + 3
            elif inmediato <= 65535 and inmediato >= -32768:
                print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta")
                return count + 4
            else:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H - {linea} Error: El parametro {param2} excede los 16 bits"
                )
        else:
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {linea} Error: No se reconoce los parametro")

    else:
        print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {linea} {componentes} Error: Argumentos invalidos")
    return count


def checkLinewithoutOperands(line, n, count):
    line = line.replace(",", " ")
    line = line.split(" ")
    if len(line) > 1:
        word = " ".join(line)
        print(
            f"{n} -  {format(count, 'x').zfill(4).upper()}H - {word} :error : esta instruccion  no admite operandos"
        )
        return count
    else:
        word = " ".join(line)
        if word == "AAA":
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {(word)} 37H ")
            return count + 1
        elif word == "AAD":
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {(word)} D50AH ")
            return count + 2
        elif word == "HLT":
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {(word)} F4H ")
            return count + 1
        elif word == "INTO":
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {(word)} CEH ")
            return count + 1
        elif word == "SCASW":
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {(word)} AFH ")
            return count + 1
        elif word == "STC":
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {(word)} F9H ")
            return count + 1


def analyzeTwoOperandsCodeSegments(
    line, tuplaNombreVariables8bits, tuplaNombresVariables16bits, n, count
):
    # Esta funcion analiza las lineas que tienen dos operandos y solo puede ser
    #  REG, MEM
    # LES
    # LDS

    line = cleanLine(line)
    componentes = line.split()
    parametro = componentes[1:]

    if len(parametro) == 2:
        if (
            parametro[0] in registros16bits
            and parametro[1] in tuplaNombresVariables16bits
        ):
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line}: Linea correcta")
            count = count + 4
            return True, count
        elif (
            parametro[0] in registros8bits and parametro[1] in tuplaNombreVariables8bits
        ):
            print(count)
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line}: Linea correcta")
            count = count + 3
            return True, count
        elif (
            parametro[0] in registros16bits
            and parametro[1] in tuplaNombreVariables8bits
        ):
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line}: Linea incorrecta no se puede operar 16 bits con 8 bits"
            )
            return True, count
        elif (
            parametro[0] in registros8bits
            and parametro[1] in tuplaNombresVariables16bits
        ):
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line}: Linea incorrecta no se puede operar 8 bits con 16 bits"
            )
            return True, count
        elif (
            parametro[0] in tuplaNombreVariables8bits
            and parametro[1] in registros16bits
        ):
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line}: Linea incorrecta no se puede operar 8 bits con 16 bits"
            )
            return True, count
        else:
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Incorrecto parametros invalidos")
            return True, count
    else:
        print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: Debe tener dos argumentos")
        return False, count


etiquetasmodificadas = []


def analyzeOneOperandCodeSegments(
    line, tuplaNombreVariables8bits, tuplaNombreVariables16bits, n, count
):
    # Esta funcion administra las instrucciones que solo tienen un operando

    # Instrucciones
    # "DEC reg/mem",
    # "IDIV reg/mem",
    # "IMUL reg/mem",
    # "POP reg/mem",
    # "dec",
    # "idiv",
    # "imul",
    # "pop",

    line = cleanLine(line)
    componentes = line.split()

    parametro = componentes[1:]

    if len(parametro) == 1:
        if parametro[0] in registros16bits:
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Linea correcta")
            count += 2
            return True, count
        elif parametro[0] in registros8bits:
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Linea correcta")
            count += 2
            return True, count
        elif parametro[0] in tuplaNombreVariables8bits:
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Linea correcta")
            count += 3
            return True, count
        elif parametro[0] in tuplaNombreVariables16bits:
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H- {line} Linea correcta")
            count += 4
            return True, count
        else:
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} variable no encontrada")
            return False, count
    else:
        print(
            f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: Instruction solo debe llevar un operando"
        )
        return False, count


def analyceJumps(
    line, n, etiquetas, tuplaNombreVariables8bits, tuplaNombresVariables16bits, count
):
    # Esta funcion analisa los saltos
    line = cleanLine(line)

    for elemento in etiquetas:
        valor = elemento[0]
        valor = valor.replace("[", "").replace("]", "")
        valor = valor.replace("'", "")
        valor = valor.upper()

        etiquetasmodificadas.append(valor)

    tuplaEtiquetas = tuple(etiquetasmodificadas)

    componentes = line.split()
    parametro = componentes[1:]

    if len(parametro) == 1:
        if parametro[0] in tuplaNombreVariables8bits:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: No se puede saltar a una variable"
            )
            return count 
        elif parametro[0] in tuplaNombresVariables16bits:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: No se puede saltar a una variable"
            )
            return count 
        elif componentes[0] == "JC":
            for etiqueta in etiquetas:
                if etiqueta[0] == parametro[0]:
                    print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} 0F82 {etiqueta[1]}H")
                    return count + 2
        elif componentes[0] == "JA":
            for etiqueta in etiquetas:
                if etiqueta[0] == parametro[0]:
                    print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} 0F87 {etiqueta[1]}H")
                    return count + 2
        elif componentes[0] == "JGE":
            for etiqueta in etiquetas:
                if etiqueta[0] == parametro[0]:
                    print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} 0F8D {etiqueta[1]}H")
                    return count + 2
        elif componentes[0] == "JNB":
            for etiqueta in etiquetas:
                if etiqueta[0] == parametro[0]:
                    print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} 0F82 {etiqueta[1]}H")
                    return count + 2
        elif componentes[0] == "JNO":
            for etiqueta in etiquetas:
                if etiqueta[0] == parametro[0]:
                    print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} 0F80 {etiqueta[1]}H")
                    return count + 2
        elif componentes[0] == "JNG":
            for etiqueta in etiquetas:
                if etiqueta[0] == parametro[0]:
                    print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} 0F8E {etiqueta[1]}H")
                    return count + 2
        else:
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: Etiqueta no encontrada")
            return count
    if len(parametro) > 1 or len(parametro) == 0:
        print(
            f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: Esta instruccion solo debe tener un operando"
        )
    return count