def salto(etiqueta_decimal, instruccion_decimal):
    if etiqueta_decimal > instruccion_decimal:
        # print("La dirección de etiqueta es mayor que la dirección de instrucción.")
        print("abajo (positivo)")
        # return etiqueta_decimal
    elif etiqueta_decimal < instruccion_decimal:
        # print("La dirección de instrucción es mayor que la dirección de etiqueta.")
        print("arriba (negativo)")
        # return instruccion_decimal
    else:
        print("La dirección de etiqueta y la dirección de instrucción son iguales.")

# create new function

def codigo_convert(codigo):
    # Convertir el código de operación binario a hexadecimal
    codigo_hex = hex(int(codigo, 2))
    return codigo_hex


def comprobar_tamaño_byte(direccion_etiqueta, direccion_instruccion, codigo):
    """e.g
    178
    10

    no:
    0178
    0010
    """
    # Convertir las direcciones hexadecimales a enteros
    etiqueta_decimal = int(direccion_etiqueta, 16)
    instruccion_decimal = int(direccion_instruccion, 16)

    # Restar el mayor menos el menor y convertir a hexadecimal
    diferencia_hex = hex(abs(etiqueta_decimal - instruccion_decimal))
    print(f"resta de los hexa: {diferencia_hex}")
    # Convertir la diferencia a decimal
    diferencia_decimal = int(diferencia_hex, 16)
    print(f"numero decimal del hexa: {diferencia_decimal}")


    # Comprobar si el resultado cabe en un byte
    if diferencia_decimal >= 0 and diferencia_decimal <= 128:
        salto(etiqueta_decimal, instruccion_decimal)
        print("corto.")
        # restar 2 a la diferencia_hex
        diferencia_hex = hex(diferencia_decimal - 2)
        # print(diferencia_hex)
        # print(codigo_convert(codigo))
        print(f"1 byte: {diferencia_hex} {codigo_convert(codigo)}")
    else:
        print("largo.")
        print(f"2 byte: {codigo_convert(codigo)} {direccion_etiqueta} ")


# Obtener las direcciones en formato hexadecimal del usuario
direccion_etiqueta = input("Ingrese la dirección de la etiqueta: ")
direccion_instruccion = input("Ingrese la dirección de la instrucción: ")
codigo = input("Ingrese el código de operación: ")

# Llamar a la función para comprobar el tamaño del byte
comprobar_tamaño_byte(direccion_etiqueta, direccion_instruccion, codigo)
