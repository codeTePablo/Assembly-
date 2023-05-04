def verificar_instruccion_adc(instruccion, tupla_registros, tupla_variables):
    componentes = instruccion.split()
    parametros = componentes[1:]

    if len(parametros) != 2:  # Si no hay 2 parametros
        return False
    else:
        if parametros[0] in tupla_registros and parametros[1] in tupla_variables:
            return True
        elif parametros[0] in tupla_variables and parametros[1] in tupla_registros:
            return True
        elif parametros[0] in tupla_registros and parametros[1] in tupla_registros:
            return True


tupla_registros = (
    "AX",
    "BX",
    "CX",
    "DX",
)

tupla_variables = {
    "var1",
    "var2",
    "var3",
}

instruccion1 = "ADC AX var1"
instruccion2 = "ADC var2 BX"
instruccion3 = "ADC CX DX"
instruccion4 = "ADC var1"
instruccion5 = "ADD AX var1"


print(verificar_instruccion_adc(instruccion1, tupla_registros, tupla_variables))
print(verificar_instruccion_adc(instruccion2, tupla_registros, tupla_variables))
print(verificar_instruccion_adc(instruccion3, tupla_registros, tupla_variables))
print(verificar_instruccion_adc(instruccion4, tupla_registros, tupla_variables))
print(verificar_instruccion_adc(instruccion5, tupla_registros, tupla_variables))


# True
