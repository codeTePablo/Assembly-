from tuples import (
    registros16bits,
    registros8bits,
    corchetes,
)
from dicts import *
from anlisisVariables import *
from functions import *


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
    line = line.replace("  ", " ")
    return line


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


def analyzeOneOperandCodeSegments(
    line, tuplaNombreVariables8bits, tuplaNombreVariables16bits,variables8bits, variables16bits, n, count
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

    instruccion = componentes[0]
    valor = instrucciones[instruccion]["valor"]
    direccion = instrucciones[instruccion]["direccion"]


  

    if parametro[0].startswith("["):
        joined_string = " ".join(parametro)
        parametro = [joined_string]

    if len(parametro) == 1:
        if parametro[0] in registros16bits:
            mod = w_es_1[parametro[0]]["mod"]
            rm = w_es_1[parametro[0]]["r/m"]
   
            direccion = instrucciones[instruccion]["direccion"]

            cambiodew = valor.replace("w", "1")
            
            direccion = direccion.replace("mod", mod)
            direccion = direccion.replace("r/m", rm)

            codificacion_binaria = cambiodew + direccion
            codificacion_binaria = codificacion_binaria.replace(" ", "")


            codificacionhex= hex(int(codificacion_binaria, 2) )[2:].upper()
            
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} -  {codificacionhex}H"
            )
            count += 2
            return True, count
        elif parametro[0] in registros8bits:
            mod = w_es_1[parametro[0]]["mod"]
            rm = w_es_1[parametro[0]]["r/m"]
   
            direccion = instrucciones[instruccion]["direccion"]

            cambiodew = valor.replace("w", "0")
            
            direccion = direccion.replace("mod", mod)
            direccion = direccion.replace("r/m", rm)

            codificacion_binaria = cambiodew + direccion
            codificacion_binaria = codificacion_binaria.replace(" ", "")


            codificacionhex= hex(int(codificacion_binaria, 2) )[2:].upper()
            
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} -  {codificacionhex}H"
            )
            count += 2
            return True, count
        elif parametro[0] in tuplaNombreVariables8bits:

            cambiodew = valor.replace("w", "0")
            direccion = instrucciones[instruccion]["direccion"]

            direccion = direccion.replace("mod", "00")
            direccion = direccion.replace("r/m", "110")

            for variables in variables8bits:
                if variables[0].upper() == parametro[0]:
                    desplazamiento = variables8bits[0][-1:]
                    

            codificacion_binaria = cambiodew + direccion 

            codificacion_binaria = codificacion_binaria.replace(" ", "")

            codificacionhex= hex(int(codificacion_binaria, 2) )[2:].upper()
            
            codificacionhex = codificacionhex + desplazamiento[0].replace("H", "")


            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} -  {codificacionhex}H"
            )
            count += 3
            return True, count
        elif parametro[0] in tuplaNombreVariables16bits:
            cambiodew = valor.replace("w", "1")
            direccion = instrucciones[instruccion]["direccion"]

            direccion = direccion.replace("mod", "00")
            direccion = direccion.replace("r/m", "110")

            for variables in variables8bits:
                if variables[0].upper() == parametro[0]:
                    desplazamiento = variables8bits[0][-1:]
                    

            codificacion_binaria = cambiodew + direccion 

            codificacion_binaria = codificacion_binaria.replace(" ", "")

            codificacionhex= hex(int(codificacion_binaria, 2) )[2:].upper()
            
            codificacionhex = codificacionhex + desplazamiento[0].replace("H", "")


            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} -  {codificacionhex}H"
            )
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H- {line} Linea correcta"
            )
            count += 4
            return True, count
        elif parametro[0] in corchetes:
            instruccion = componentes[0]
            valor = instrucciones[instruccion]["valor"]
            direccion = instrucciones[instruccion]["direccion"]
            mod = tabla_d[parametro[0]]["mod"]
            rm = tabla_d[parametro[0]]["r/m"]


            cambiodew = valor.replace("w", "0")
            direccion = direccion.replace("mod", mod)
            direccion = direccion.replace("r/m", rm)

            codificacion_binaria = cambiodew + direccion
            codificacion_binaria = codificacion_binaria.replace(" ", "")
            
            codificacionhex= hex(int(codificacion_binaria, 2) )[2:].upper()

            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} - {codificacionhex}H"
            )

            count += 1
            return True, count

        else:
            parametros = parametro[0].split()
            if parametros[0].startswith("["):
                ultimoParametro = parametros[-1]
                ultimo_numero = (
                    ultimoParametro.replace("]", "").replace("[", "").replace("+", " ")
                )
                numeros = [c for c in ultimo_numero if c.isdigit()]
                numeros = "".join(numeros)
                ultimo_numero = convertir_a_decimal(numeros)
                ultimo_numero = str(ultimo_numero)

                if ultimo_numero.isdigit() == True:
                    numero = convertir_a_decimal(ultimo_numero)
                    if -127 <= numero <= 128:
                        rm = revisarCorchetes(parametros)
                        mod= "01"
                        direccion = instrucciones[instruccion]["direccion"]

                        direccion = direccion.replace("mod", mod)
                        direccion = direccion.replace("r/m", rm)
                        cambiodew = valor.replace("w", "0")

                        desplazamiento = convertir_a_hexa(str(numero))

                        codificacion_binaria = cambiodew + direccion 
                        codificacion_binaria = codificacion_binaria.replace(" ", "")

                        codificacionhex= hex(int(codificacion_binaria, 2) )[2:].upper()

                        codificacionhex = codificacionhex + desplazamiento

                        print(
                            f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} correcto: 8 bits - {codificacionhex}H"
                        )

                        return True, count + 1
                    elif -32767 <= numero <= 32768:
                        rm = revisarCorchetes(parametros)
                        mod= "10"
                        direccion = instrucciones[instruccion]["direccion"]

                        direccion = direccion.replace("mod", mod)
                        direccion = direccion.replace("r/m", rm)
                        cambiodew = valor.replace("w", "0")

                        desplazamiento = convertir_a_hexa(str(numero))

                        codificacion_binaria = cambiodew + direccion 
                        codificacion_binaria = codificacion_binaria.replace(" ", "")

                        codificacionhex= hex(int(codificacion_binaria, 2) )[2:].upper()

                        codificacionhex = codificacionhex + desplazamiento

                        print(
                            f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} {codificacionhex}H"
                        )
                        return True, count + 1
                    else:
                        print(
                            f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} incorrecto: "
                        )
                        return False, count
                else:
                    print(
                        f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} incorrecto: "
                    )
                    return True, count + 1
            else:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} variable no encontrada"
                )
                return False, count
    else:
        print(
            f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: Instruction solo debe llevar un operando"
        )
        return False, count


def analyzeOperandsCodeSegments(
     line, tuplaNombreVariables8bits, tuplaNombresVariables16bits, n, count, variables8bits, variables16bits
            
):
    # Esta funcion analiza las lineas que tienen dos operandos del orden
    # REG, memory
    # memory, REG
    # REG, REG
    # memory, immediate
    # REG, immediate

    line = cleanLine(line)
    componentes = line.split()
    parametro = componentes[1:]

    print(componentes)

    instruccion = componentes[0]
    print(instruccion)

    if len(parametro) == 2:
        param1 = parametro[0]
        param2 = parametro[1]

        if param1 in registros16bits and param2 in tuplaNombresVariables16bits:
            print(
                f"{n} -   {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta"
            )
            return count + 4
        elif param1 in tuplaNombresVariables16bits and param2 in registros16bits:
            print(
                f"{n} -   {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta"
            )
            return count + 4
        elif param1 in registros8bits and param2 in tuplaNombreVariables8bits:
            print(
                f"{n} -   {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta"
            )
            return count + 3
        elif param1 in tuplaNombreVariables8bits and param2 in registros8bits:
            print(
                f"{n} -   {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta"
            )
            return count + 3
        elif param1 in registros16bits and param2 in registros16bits:
            print(
                f"{n} -   {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta"
            )
            return count + 2
        elif param1 in registros8bits and param2 in registros8bits:
            print(
                f"{n} -   {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta"
            )
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
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta"
                )
                return count + 3
            else:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: El parametro {param2} excede los 8 bits"
                )
        elif param1 in registros16bits:
            if inmediato > 255 and inmediato < -128:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta"
                )
                return count + 3
            elif inmediato <= 65535 and inmediato >= -32768:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta"
                )
                return count + 4
            else:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H -{line} Error: El parametro {param2} excede los 16 bits"
                )

        elif param1 in tuplaNombreVariables8bits:
            inmediato = convertir_a_decimal(param2)
            if inmediato <= 255 and inmediato >= -128:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta"
                )
                return count + 1
            else:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H  - {line} Error: El parametro {param2} excede los 8 bits"
                )
        elif param1 in tuplaNombresVariables16bits:
            if inmediato > 255 and inmediato < -128:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta"
                )
                return count + 3
            elif inmediato <= 65535 and inmediato >= -32768:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :Linea correcta"
                )
                return count + 4
            else:
                print(
                    f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: El parametro {param2} excede los 16 bits"
                )
        else:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: No se reconoce los parametro"
            )

    else:
        print(
            f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} {componentes} Error: Argumentos invalidos"
        )
    return count


def analyzeTwoOperandsCodeSegments(
   line, tuplaNombreVariables8bits, tuplaNombresVariables16bits, variables8bits, variables16bits,n, count
):
    # Esta funcion analiza las lineas que tienen dos operandos y solo puede ser
    #  REG, MEM

    # LES
    # LDS

    line = cleanLine(line)
    componentes = line.split()
    parametro = componentes[1:]

    instruccion = componentes[0]
    print(instruccion)

    if len(parametro) >= 2:
        if parametro[1].startswith("["):
            joined_string = " ".join(parametro)
            parametro2 = [joined_string]
            lista = parametro2[0].split("[")
            parametro[1] = "[" + lista[1]
            del parametro[2:]

    if len(parametro) == 2:
        if (
            parametro[0] in registros16bits
            and parametro[1] in tuplaNombresVariables16bits
        ):
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line}: Linea correcta"
            )
            count = count + 4
            return True, count
        elif (
            parametro[0] in registros8bits and parametro[1] in tuplaNombreVariables8bits
        ):
            print(count)
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line}: Linea correcta"
            )
            count = count + 3
            return True, count
        elif parametro[0] in registros8bits and parametro[1] in corchetes:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line}: Linea correcta"
            )

            return True, count
        elif parametro[0] in registros16bits and parametro[1] in corchetes:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line}: Linea correcta"
            )

            return True, count
        elif parametro[0] in tuplaNombresVariables16bits and parametro[1] in corchetes:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line}: Linea correcta"
            )

            return True, count
        elif parametro[0] in tuplaNombreVariables8bits and parametro[1] in corchetes:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line}: Linea correcta"
            )

            return True, count
        elif (
            parametro[0] in registros16bits
            and parametro[1] in tuplaNombreVariables8bits
        ):
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line}: Linea incorrecta no se puede operar 16 bits con 8 bits"
            )
            return False, count
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
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Incorrecto parametros invalidos"
            )
            return True, count
    else:
        print(
            f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: Debe tener dos argumentos"
        )
        return False, count


def analyceJumps(
    line, n, etiquetas, tuplaNombreVariables8bits, tuplaNombresVariables16bits, count
):
    # Esta funcion analiza los saltos

    etiquetasmodificadas = []
    line = cleanLine(line)

    for elemento in etiquetas:
        valor = elemento[0]
        valor = valor.replace("[", "").replace("]", "")
        valor = valor.replace("'", "")
        valor = valor.upper()

        etiquetasmodificadas.append(valor)

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

        elif parametro[0] in etiquetasmodificadas:
            if componentes[0] in saltos:
                codigo = saltos[componentes[0]]["Codificacion"]
                for etiqueta in etiquetas:
                    if etiqueta[0] == parametro[0]:
                        print(
                            f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} {codigo} {etiqueta[1]}H"
                        )
                        return count + 2
        else:
            print(
                f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: Etiqueta no encontrada"
            )
            return count
    if len(parametro) > 1 or len(parametro) == 0:
        print(
            f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} Error: Esta instruccion solo debe tener un operando"
        )
    return count
