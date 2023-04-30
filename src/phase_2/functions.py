# provando si es que podemos crear funciones externas para que el codigo no sea pesado de leer 

def add_list(my_list, lines, line):
    my_list.append(line)
    new_line = lines[lines.index(line) + 1]
    return new_line

def line_step(lines, line):
    new_line = lines[lines.index(line) + 1]
    return new_line