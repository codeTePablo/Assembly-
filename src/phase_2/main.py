from tkinter import *
from tkinter import filedialog
from tuples import *
from functions import *
from prettytable import PrettyTable

# Restructuración de código  

# Open file 
def open_file():
    """ Abre el archivo y lo lee """
    filepath = filedialog.askopenfilename(
        filetypes=[("ASM", "*.asm*"), ("Text Files", "*.txt")]
    )
    file = open(filepath, "r")
    return file.read()


def search_etiquetas(lines):
    """ Busca las etiquetas en el código y las guarda en una lista 
    args:
        lines (str): Código del archivo abierto
    return:
        list: Lista de listas con las etiquetas
    """
    lines = lines.split("\n")
    listadeEtiquetas = []
    for line in lines:
        if line.endswith(":") == True:
            etiqueta = []
            etiqueta.append(line)
            etiqueta.append("Etiqueta")
            etiqueta.append("null")  # la etiqueta no tiene tamaño
            etiqueta.append("null")  # la etiqueta no tiene valor
            listadeEtiquetas.append(etiqueta)
    # print("lista de etiquetas: " + str(listadeEtiquetas))
    return listadeEtiquetas


def fill_data_segment(lines):
    """
    Args:
        lines (str): Código del archivo abierto
    Return:
        list: Lista de listas con los datos del segmento de datos
    """
    lines = lines.split("\n")

    for line in lines:
        dataSegment = []
        if line.startswith("data segment") == True:
            # line = lines[lines.index(line) + 1]
            line = line_step(lines, line)
            while line.endswith("ends") == False:
                # dataSegment.append(line)
                # line = lines[lines.index(line) + 1]
                line = add_list(dataSegment, lines, line)
            lists = analyze_data_segment(dataSegment)
            return lists


def analyze_data_segment(dataSegment):
    """
    Analiza el segmento de datos y crea una lista de listas con los datos
    args:
        dataSegment (list): Lista de listas con los datos del segmento de datos
    """
    lists = []

    for line in dataSegment:
        # print(line + "--> Desde analizador de Data Segment")
        words = line.split(" ")

        ls = []
        # posiblemente crear una tupla con los tipos de datos y evitar tantos if
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
    lists = create_table(lists)
    return lists


def analyze_stack_segment(stackSegment):
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


def stack_segment(lines):
    lines = lines.split("\n")
    for line in lines:
        stackSegment = []
        if line.startswith("stack segment") == True:
            line = lines[lines.index(line) + 1]
            while line.endswith("ends") == False:
                stackSegment.append(line)
                line = lines[lines.index(line) + 1]
            result = analyze_stack_segment(stackSegment)
            return result


def define_code_segment(codeSegment):
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


# Despues de analizar el data segment, stack segment, code segment se crea la tabla
def create_table(lists):
    """ 
    Crea la tabla con 4 columnas 
    - simbolos
    - tipo
    - tamaño
    - valor 
    """
    table = PrettyTable(["Simbolo", "Tipo", "Tamaño", "Valor"])

    etiquetas = search_etiquetas(lines)

    for etiqueta in etiquetas:
        lists.append(etiqueta)

    for list in lists:
        table.add_row(list)

    print(table)
    return lists


if __name__ == "__main__":
    lines = open_file()

    # Lista de variables y simbolos
    lists = fill_data_segment(lines)

    # Analisis de stack segment
    bool = stack_segment(lines)

    # Analisis de code segment
    define_code_segment(lines)

    # print(lists[1][3])

    # print(lists)
