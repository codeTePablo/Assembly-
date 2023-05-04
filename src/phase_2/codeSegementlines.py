from tuples import (
    registros16bits,
    registros8bits,
)


def cleanLine(line):
    line = line.replace(",", " ").rstrip().lstrip()
    line = line.replace("  ", " ")
    return line


# def analyzeOperandsCodeSegments(linea, tupla Variables):


def analyzeOperandsCodeSegments(linea, variables):
    linea = cleanLine(linea)
    componentes = linea.split()
    parametros = componentes[1:]
    if len(parametros) != 2:  # Si no hay 2 parametros
        return False
    else:
        if parametros[0] in registros16bits and parametros[1] in variables:
            return True
        elif parametros[0] in variables and parametros[1] in registros16bits:
            return True
        elif parametros[0] in registros16bits and parametros[1] in registros16bits:
            return True
        elif parametros[0] in registros8bits and parametros[1] in variables:
            return True
        elif parametros[0] in variables and parametros[1] in registros8bits:
            return True
        elif parametros[0] in registros8bits and parametros[1] in registros8bits:
            return True
        elif parametros[0] in variables and parametros[1] in variables:
            return True
        else:
            return False


def analyzeoneOperandCodeSegments(line, variables):
    line = cleanLine(line)
    componentes = line.split()
    parametros = componentes[1:]
    if len(parametros) != 1:  # Si no hay 1 parametro
        return False
    else:
        if parametros[0] in registros16bits:
            return True
        elif parametros[0] in registros8bits:
            return True
        elif parametros[0] in variables:
            return True
        else:
            return False
