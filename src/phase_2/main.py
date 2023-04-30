from tkinter import *
from tkinter import filedialog
from tuples import *
from prettytable import PrettyTable


def openFile():
    filepath = filedialog.askopenfilename(
        filetypes=[("ASM", "*.asm*"), ("Text Files", "*.txt")]
    )
    file = open(filepath, "r")
    return file.read()


def fillDataSegment(lines):
    lines = lines.split("\n")

    for line in lines:
        dataSegment = []
        if line.startswith("data segment") == True:
            line = lines[lines.index(line) + 1]
            while line.endswith("ends") == False:
                dataSegment.append(line)
                line = lines[lines.index(line) + 1]
            lists = analyzeDatasegment(dataSegment)
            return lists


def searchEtiquetas(lines):
    lines = lines.split("\n")
    listadeEtiquetas = []
    for line in lines:
        if line.endswith(":") == True:
            etiqueta = []
            etiqueta.append(line)
            etiqueta.append("Etiqueta")
            etiqueta.append("null")
            etiqueta.append("null")
            listadeEtiquetas.append(etiqueta)

    return listadeEtiquetas


def analyzeDatasegment(dataSegment):
    lists = []

    for line in dataSegment:
        # print(line + "--> Desde analizador de Data Segment")
        words = line.split(" ")

        ls = []

        for word in words:
            if word == (""):
                pass
            elif word.startswith("EQU"):
                ls.append("Constante")
                ls.append("dw")
            elif word.startswith("equ"):
                ls.append("Constante")
                ls.append("dw")
            elif word.startswith(pseudoinstruction):
                ls.append("Variable")
                ls.append(word)

            elif word.startswith(numbers):
                ls.append(word)
            elif word.startswith("-"):
                ls.append(word)
            elif word.startswith('"' or "'"):
                str = ""
                string = []
                while word.endswith('"' or "'") == False:
                    string.append(word)
                    word = words[words.index(word) + 1]
                string.append(word)
                for word in string:
                    str = str + word + " "
                ls.append(str)
                break
            elif word.startswith("DUP"):
                str = ""
                string = []
                while word.endswith(")") == False:
                    string.append(word)
                    word = words[words.index(word) + 1]
                string.append(word)
                for word in string:
                    str = str + word + " "
                ls.append(str)
                break
            elif word.startswith("dup"):
                str = ""
                string = []
                while word.endswith(")") == False:
                    string.append(word)
                    word = words[words.index(word) + 1]
                string.append(word)
                for word in string:
                    str = str + word + " "
                ls.append(str)
                break
            elif word.startswith(abecedario):
                ls.append(word)

        for word in ls:
            if word == (space):
                ls.remove(word)

        if len(ls) < 4:
            print("Error en la linea: " + line + " Falta de argumentos")
        if len(ls) > 4:
            print("Error en la linea: " + line + " Exceso de argumentos argumentos")
        if len(ls) == 4:
            lists.append(ls)

        for word in ls:
            if word.startswith("-"):
                if ls[2] == ("db"):
                    valor = int(ls[3])
                    if valor < -129:
                        print(
                            "Error en la linea: "
                            + line
                            + " El valor no puede ser menor a -129"
                        )
                        lists.remove(ls)
                elif ls[2] == ("dw"):
                    valor = int(ls[3])
                    if valor < -32769:
                        print(
                            "Error en la linea: "
                            + line
                            + " El valor no puede ser menor a -32769"
                        )
                        lists.remove(ls)
            elif word.startswith(numbers):
                if ls[2] == ("db"):
                    valor = int(ls[3])
                    if valor > 255:
                        print(
                            "Error en la linea: "
                            + line
                            + " El valor no puede ser mayor a 255"
                        )
                        lists.remove(ls)
                elif ls[2] == ("dw"):
                    valor = int(ls[3])
                    if valor > 65535:
                        print(
                            "Error en la linea: "
                            + line
                            + " El valor no puede ser mayor a 65535"
                        )
                        lists.remove(ls)
    lists = createTable(lists)
    return lists


def createTable(lists):
    table = PrettyTable(["Simbolo", "Tipo", "Tamaño", "Valor"])

    etiquetas = searchEtiquetas(lines)

    for etiqueta in etiquetas:
        lists.append(etiqueta)

    # print(lists)

    for list in lists:
        table.add_row(list)

    print(table)
    return lists


def analyzeStackSegment(stackSegment):
    ls = []
    words = "".join(stackSegment)
    words = words.split(" ")

    for word in words:
        if word == (""):
            pass
        else:
            ls.append(word)

    if ls[0].startswith("db"):
        valor = int(ls[1])
        if valor > 255:
            print("Error en la linea: " + ls[0] + " El valor no puede ser mayor a 255")
            return False
        else:
            return True
    elif ls[0].startswith("dw"):
        valor = int(ls[1])
        if valor > 65535:
            print(
                "Error en la linea: " + ls[0] + " El valor no puede ser mayor a 65535"
            )
            return False
        else:
            return True


def stackSegment(lines):
    lines = lines.split("\n")
    for line in lines:
        stackSegment = []
        if line.startswith("stack segment") == True:
            line = lines[lines.index(line) + 1]
            while line.endswith("ends") == False:
                stackSegment.append(line)
                line = lines[lines.index(line) + 1]
            result = analyzeStackSegment(stackSegment)
            return result


def defineCodesegmen(codeSegment):
    lines = codeSegment.split("\n")

    codeSegment = []
    for line in lines:
        if line.startswith("code segment") == True:
            line = lines[lines.index(line) + 1]
            while line.endswith("ends") == False:
                if line == "\n" == True:
                    print("Error en la linea: " + line + " Falta de argumentos")
                    pass
                else:
                    codeSegment.append(line)
                    line = lines[lines.index(line) + 1]
    print(codeSegment)


lines = openFile()

# Lista de variables y simbolos
lists = fillDataSegment(lines)

# Analisis de stack segment
bool = stackSegment(lines)

# Analisis de code segment
defineCodesegmen(lines)

print(lists[1][3])

print(lists)
