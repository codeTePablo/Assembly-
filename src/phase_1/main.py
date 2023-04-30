from tkinter import *
from tkinter import filedialog
from tuples import *
import keyboard


def openFile():
    filepath = filedialog.askopenfilename(
        filetypes=[("ASM", "*.asm*"), ("Text Files", "*.txt")]
    )
    file = open(filepath, "r")
    return file.read()


lines = openFile()
print(lines)
lines = lines.split("\n")

print("\n Identificacion \n")
ins = []

while True:
    for i, line in enumerate(lines, start=1):
        line = line.split(";")[0].strip()
        if line.startswith(pseudoinstruction) == True:
            print(f"{i}- {line}: pseudoinstruction")
        elif line == "":
            pass

        else:
            words = line.replace(", ", " ").split(" ")

            for n in words:
                if n in pseudoinstruction:
                    print(f"{i}- {n}: pseudoinstruction")
                    ins.append(n)
                elif n in registros:
                    print(f"{i}- {n}: registro")
                    ins.append(n)
                elif n in instrucciones:
                    print(f"{i}- {n}: instrucción")
                    ins.append(n)

                else:
                    string = ""
                    if n.startswith('"' or "'") == True:
                        ls = []
                        while n.endswith('"' or "'") == False:
                            ls.append(n)
                            n = words[words.index(n) + 1]
                        ls.append(n)

                        for elem in ls:
                            string = string + " " + elem
                        print(f"{i}- {string}: constante caracter")

                        for item in ls:
                            if item in words:
                                words.remove(item)

                    if n.startswith(numbers):
                        lsn = []
                        lsn.append(n)
                        if n.endswith("h"):
                            print(f"{i}- {n}: constante numerica hexadecimal")
                        if n.endswith("H"):
                            print(f"{i}- {n}: constante numerica hexadecimal")
                        elif n.endswith("B"):
                            print(f"{i}- {n}: constante numerica binaria")
                        elif n.endswith("b"):
                            print(f"{i}- {n}: constante numerica binaria")
                        elif n.endswith(abecedario):
                            print(f"{i}- {n}: caracter no valido")
                        else:
                            print(f"{i}- {n}: constante numerica decimal")

                        for item in words:
                            for item_1 in lsn:
                                if item == item_1:
                                    words.remove(item)

                    if n.startswith("["):
                        ls = []
                        ls.append(n)

                        while not n.endswith("]"):
                            n = words[words.index(n) + 1]
                            ls.append(n)

                        for elem in ls:
                            if elem in pseudoinstruction:
                                print(f"{i}- {str(ls)}: pseudo-instrucción de memoria")
                            elif elem in instrucciones:
                                print(f"{i}- {str(ls)}: instrucción de memoria")
                            elif elem in registros:
                                print(f"{i}- {str(ls)}: registro")
                            elif elem in numbers:
                                print(f"{i}- {str(ls)}: coonstante numerica")
                        print(f"{i}- {str(ls)}: instrucción de memoria")

                        for item in words:
                            for item_1 in ls:
                                if item == item_1:
                                    words.remove(item)

                    if n.startswith("dup("):
                        ls = []
                        while n.endswith(")") == False:
                            ls.append(n)
                            n = words[words.index(n) + 1]
                        ls.append(n)

                        for elem in ls:
                            string = string + " " + elem
                        print(f"{i}- {string}: pseudo-instrucción dup")

                        for item in words:
                            for item_1 in ls:
                                if item == item_1:
                                    words.remove(item)

                    elif n.startswith(abecedario):
                        if len(n) > 10:
                            print(f"{i}- {n}: caracter no valido")
                        else:
                            print(f"{i}- {n}: simbolo")
                    else:
                        pass

    print("Presione ESC para salir")
    keyboard.wait("esc")
    break
