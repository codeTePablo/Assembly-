
def table():
    # crear tabla
    # BUSCAR en la tabla
    # retorne el mod y el r/m
    mod = 1
    rm = 1
    return mod, rm

def fsafa():
    mod, rm = table()
    print(mod)
    print(rm)
    intrucciones_1 = {
        'push': {'valor':{},  'operandos':{'reg o mem'}, 'mod':{}}
    }

    diccionario_principal = {
    'push': {
        mod,
        rm,
        }
    }
    print(diccionario_principal)

fsafa()