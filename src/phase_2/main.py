from tkinter import *
from tkinter import filedialog
from tuples import *
from functions import *
from prettytable import PrettyTable

# Restructuración de código


# Open file
def open_file():
    """Abre el archivo y lo lee"""
    filepath = filedialog.askopenfilename(
        filetypes=[("ASM", "*.asm*"), ("Text Files", "*.txt")]
    )
    file = open(filepath, "r")
    return file.read()


def search_etiquetas(lines: list) -> list:
    """Busca las etiquetas en el código y las guarda en una lista
    args:
        lines (str): Código del archivo abierto
    return:
        list: Lista de listas con las etiquetas
    """
    lines = lines.split("\n")
    listadeEtiquetas = []
    for line in lines:
        if line.endswith(":") == True:
            etiqueta = tags(line)
            listadeEtiquetas.append(etiqueta)
    # print("lista de etiquetas: " + str(listadeEtiquetas))
    return listadeEtiquetas


def fill_data_segment(lines):
    """
    Args:
        lines (str): Identifica cuando es que empieza el segmento de datos
    Return:
        list: Lista de listas con los datos del segmento de datos
    """
    lines = lines.split("\n")

    for line in lines:
        dataSegment = []
        if line.startswith("data segment"):
            line = line_step(lines, line)
            while line.endswith("ends") == False:
                if line.startswith(numbers):
                    print(
                        "Error en la linea: "
                        + line
                        + " No se puede declarar con un numero al inicio"
                    )
                elif line.startswith(pseudoinstruction):
                    print(
                        f"Error en la linea: {line} No se puede declarar con una pseudoinstruccion al inicio"
                    )
                    break
                else:
                    line = add_list(dataSegment, lines, line)
            clean_data_segment = list(filter(str.strip, dataSegment))

            return analyze_data_segment(clean_data_segment)


def analyze_data_segment(clean_data_segment: list) -> list:
    """
    Analiza el segmento de datos y crea una lista de listas con los datos
    args:
        dataSegment (list): Lista de listas con los datos del segmento de datos
    """
    # print(lists[0]) #imprime el primer elemento de la lista de listas
    return create_table(data_segment(clean_data_segment))


def analyze_stack_segment(stackSegment):
    """
    Analiza el segmento de pila y crea una lista de listas con los datos
    args:
        stackSegment (list): Lista de listas con los datos del segmento de pila
    """
    return stack_Segment(stackSegment)


def stack_segment(lines):
    lines = lines.split("\n")
    for line in lines:
        stackSegment = []
        if line.startswith("stack segment") == True:
            line = lines[lines.index(line) + 1]
            while line.endswith("ends") == False:
                line = add_list(stackSegment, lines, line)
            result = analyze_stack_segment(stackSegment)
            return result


def define_code_segment(codeSegment):
    lines = codeSegment.split("\n")
    # print(type(lines))
    in_code_segment = False
    code_segment = []
    for line in lines:
        if "code segment" in line:
            lines = True
        elif "ends" in line:
            lines = False
        elif lines and line.strip() != "":
            code_segment.append(line.strip())
    return code_segment


# Despues de analizar el data segment, stack segment se crea la tabla
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

    # Analisis de stack segment regresa un false o true en caso de que el stack segment este bien o mal
    boleano = stack_segment(lines)

    # Analisis de code segment
    codesegment = define_code_segment(lines)

    #
    print(lists)
    print(boleano)
    print(codesegment)
