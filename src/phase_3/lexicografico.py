from tkinter import *
from tkinter import filedialog
from tuples_lex import *
import keyboard

def lexicogtaphic():
        def openFile():
            filepath = filedialog.askopenfilename(
                filetypes=[("ASM", "*.asm*"), ("Text Files", "*.txt")]
            )
            file = open(filepath, "r")
            return file.read()


        def analyzer2(linea):
            words = linea.split(" ")
            for word in words:
                if word in pseudoinstruction:
                    print(f"{i}- {word}: pseudoinstruction")
                elif word in registros:
                    print(f"{i}- {word}: registro")
                elif word in instrucciones:
                    print(f"{i}- {word}: instrucción")
                elif word in registros:
                    print(f"{i}- {word}: registro")
                elif word.startswith(abecedario):
                    if len(word) > 10:
                        print(f"{i}- {word}: caracter no valido")
                    else:
                        print(f"{i}- {word}: simbolo")
                elif word.startswith(numbers):
                    print(f"{i}- {word}: constante numerica ")
                else:
                    try:
                        analyzeCorchete2(word)
                    except:
                        print (f"{i}- {word}: simbolo no valido")


        def analyzeCorchete2(word):
            word = (
                word.replace("[", "")
                .replace("]", "")
                .replace("+", " ")
                .replace("-", " ")
                .replace("*", " ")
                .replace("/", " ")
            )
            word = word.split(" ")

            for elem in word:
                if elem in pseudoinstruction:
                    print(f"{i}- {elem}: pseudoinstruction")
                elif elem in registros:
                    print(f"{i}- {elem}:  registro")
                elif elem in instrucciones:
                    print(f"{i}- {elem}: instrucción")
                elif elem.isdigit():
                    print(f"{i}- {elem}: constante numerica")


        def analyzeCorchete(ls):
            for elem in ls:
                elem = elem.replace("[", "").replace("]", "")
                if elem in pseudoinstruction:
                    print(f"{i}- {elem}: pseudoinstruction")
                elif elem in registros:
                    print(f"{i}- {elem}:  registro")
                elif elem in instrucciones:
                    print(f"{i}- {elem}: instrucción")
                elif elem in numbers:
                    print(f"{i}- {elem}: constante numerica decimal")
        lines = openFile()
        linestoexport = lines
        print(lines)
        lines = lines.split("\n")

        print("\n Identificacion \n")
        ins = []
        for i, line in enumerate(lines, start=0):
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
                            try:
                                while not n.endswith("]"):
                                    n = words[words.index(n) + 1]
                                    ls.append(n)
                                try:
                                    analyzeCorchete(ls)
                                except:
                                    print(f"{i}- {n}: caracter no valido")
                                for item in words:
                                    for item_1 in ls:
                                        if item == item_1:
                                            words.remove(item)
                            except:
                                print(f"{i}- {n}: caracter no valido")
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
                                sincoma = n.replace(",", " ")
                                try:
                                    analyzer2(sincoma)
                                except:
                                    print(f"{i}- {n}: caracter no valido")
                            else:
                                sincoma = n.replace(",", " ")
                                try:
                                    analyzer2(sincoma)
                                except:
                                    print(f"{i}- {n}: caracter no valido")
                        else:
                            pass
        return linestoexport


