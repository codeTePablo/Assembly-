from tuples import *
from dicts import *
import re


def add_list(my_list, lines, line):
    my_list.append(line)
    new_line = lines[lines.index(line) + 1]
    return new_line


def line_step(lines, line):
    new_line = lines[lines.index(line) + 1]
    return new_line


def append_to_list():
    pass


def tags(line):
    etiqueta = []
    etiqueta.append(line)
    etiqueta.append("Etiqueta")
    etiqueta.append("null")  # la etiqueta no tiene tamaño
    etiqueta.append("null")  # la etiqueta no tiene valor
    return etiqueta


def binary_numbers(binario):
    # binario = "10101010B"
    decimal = int(binario[:-1], 2)
    print(f"{decimal} es decimal")


def new_list_for_memory(line):
    new_list = [[x[0]] for x in line]
    # print(f"la nueva lista: {new_list}")
    return new_list


def create_list_for_instructions(line):
    # codigo = "ADC AX, BX"
    # lista = ["ADC", "AX", "BX"]
    lista = line.split(" ")
    for i in range(len(lista)):
        lista[i] = lista[i].replace(",", "")
    # print(lista)
    return lista


def check_order_istructions(line, lista_memoria):
    print(line)
    print(lista_memoria)
    # exit()
    """verificamos que las instrucciones esten en orden
    args:
        instructios: es un diccionario con las instrucciones
        line: es la linea que se esta analizando
    e.g
    ADC = [REG, memory]
    IDIV = [REG]
    """
    # print(line)
    instruction = line[0]
    valores = line[1:]
    print(len(valores))
    if len(valores) == 1:
        if instruction in instrucciones_a_checar.instrucciones:
            reg, memory = instrucciones_a_checar.instrucciones[instruction][0]
            if all(valor in reg for valor in valores if valor not in memory) and all(
                valor in memory for valor in valores if valor not in reg
            ):
                print(f"la instruccion: {instruction} son correctos")
            elif all(valor in memory for valor in valores if valor not in reg):
                print("Los valores de memoria son correctos")
            else:
                print("Error: los valores no están en el orden correcto")
        else:
            print("Error: instrucción desconocida")

    # elif len(valores) >= 1:
    #     if instruction in instrucciones:
    #         reg = instrucciones[instruction][0]
    #         mem = instrucciones[instruction][1]
    #         if all(valor in reg for valor in valores) or all(
    #             valor in mem for valor in valores
    #         ):
    #             print(f"la instruccion: {instruction} son correctos")
    #         else:
    #             print("Error: los valores no están en el orden correcto")


# analyze


def type_table_constant(my_list):
    my_list.append("Constante")
    my_list.append("dw")
    return my_list


def type_table_variable(my_list, word):
    my_list.append("Variable")
    my_list.append(word)
    return my_list


def data_segment(dataSegment):
    lists = []

    for line in dataSegment:
        words = line.split(" ")

        ls = []
        for word in words:
            if word == (space):
                pass
            elif word.startswith(data_segment_words):
                type_table_constant(ls)
            elif word.startswith(pseudoinstruction):
                type_table_variable(ls, word)
            elif word.startswith(numbers):
                ls.append(word)
            elif word.startswith("-"):
                ls.append(word)
            elif word.startswith('"' or "'"):
                new_str = ""
                string = []
                while word.endswith('"' or "'") == False:
                    word = add_list(string, words, word)
                string.append(word)
                for word in string:
                    new_str = new_str + word + " "
                ls.append(new_str)
                break
            elif word.startswith(data_segment_words_2):
                new_str = ""
                string = []
                while word.endswith(")") == False:
                    word = add_list(string, words, word)
                string.append(word)
                for word in string:
                    new_str = new_str + word + " "
                ls.append(new_str)
                break
            elif word.startswith(abecedario):
                ls.append(word)

        for word in ls:
            if word == (space):
                ls.remove(word)

        if len(ls) == 0:
            pass
        if len(ls) < 4:
            print("Error en data segment la linea: " + line + " Falta de argumentos")
        if len(ls) > 4:
            print(
                "Error en data segment la linea: "
                + line
                + " Exceso de argumentos argumentos"
            )
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
                    #
                    valor = ls[3]
                    print(valor)
                    # valor = int(ls)
                    valor_1 = binary_numbers(valor)
                    print(valor_1)
                    if valor > 255:
                        print(
                            f"Error en la linea: {line} El valor no puede ser mayor a 255"
                        )
                        lists.remove(ls)
                    else:
                        pass
                        # print("OK")
                elif ls[2] == ("dw"):
                    valor = int(ls[3])
                    if valor > 65535:
                        print(
                            "Error en la linea: "
                            + line
                            + " El valor no puede ser mayor a 65535"
                        )
                        lists.remove(ls)
    return lists


def stack_Segment(stackSegment):
    ls = []
    words = "".join(stackSegment)
    words = words.split(" ")
    words = list(filter(None, words))

    line = " ".join(words)

    if line.startswith("db"):
        if int(words[1]) <= 255:
            return "OK"
        else:
            return "Error en stack segment se supera el valor de los 8 bits"
    elif line.startswith("dw"):
        if int(words[1]) <= 65535:
            return "OK"
        else:
            return "Error en stack segment se supera el valor de los 8 bits"

    else:
        print("Error en la linea: " + line + " linea no valida")


def CheckingEtiqueta(etiqueta):
    patron = r"^(?P<etiqueta>[a-zA-Z_]\w*\s*):$"
    coincidencias = re.search((patron), etiqueta)
    if coincidencias:
        return True
    else:
        return False


if __name__ == "__main__":
    # line = ["DEC", "[BX+SI]"]  # OK
    # line = ["DEC", "hola"]  # error
    # line = ["ADC", "BX"] # OK
    # line = ["ADC", "BX", "[SI]"]  # error
    # line = ["LES", "AX", "[BX]"]  # fuera de rango
    line = [["ADC", "[SI+immediate]", "AX"], ["ADC", "BX", "[SI]"]]

    # check_order_istructions(line)
    check_order_istructions(
        line,
    )
