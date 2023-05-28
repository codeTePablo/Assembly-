# Proyecto de Ensamblador EMU 8086

Este proyecto de ensamblador está desarrollado para trabajar con el EMU 8086, un emulador de procesador Intel 8086. El código del proyecto consta de tres fases principales, cada una con funcionalidades específicas.

## Fase 1: Detección de Instrucciones

En la primera fase, el programa se encarga de detectar las instrucciones presentes en el código fuente. Esta fase se encarga únicamente de identificar las instrucciones, sin realizar ningún tipo de validación adicional. Es el punto de partida para el análisis del código.

## Fase 2: Validación de Instrucciones y Sintaxis

La segunda fase del proyecto tiene como objetivo reconocer ciertas instrucciones y verificar si la sintaxis es correcta. Además, se realiza la validación de las variables utilizadas en el código. Esta fase asegura que las instrucciones sean reconocidas correctamente por el ensamblador y que la sintaxis cumpla con los requisitos del lenguaje.

Durante esta fase, se comprueba que las variables utilizadas estén declaradas previamente y que sean utilizadas de manera correcta. Se verifica que los registros y operaciones utilizados sean válidos y estén dentro de los límites permitidos. En caso de encontrar algún error de sintaxis o uso incorrecto de variables, se generarán mensajes de error correspondientes.

## Fase 3: Generación de Contadores Hexadecimales y Codificación de Instrucciones

La tercera fase se encarga de crear un contador hexadecimal para cada línea de código y determinar si está correctamente formada o no. Además, esta fase es responsable de codificar ciertas instrucciones, especialmente las instrucciones de salto.

En esta fase, se generan los contadores hexadecimales para cada línea de código y se comprueba si se cumplen los requisitos de longitud y formato establecidos. Además, se lleva a cabo la codificación de las instrucciones de salto, ajustando las direcciones de destino según sea necesario.

## Uso del Proyecto

Para utilizar este proyecto de ensamblador sobre el EMU 8086, sigue estos pasos:

1. Prepara tu código fuente en lenguaje ensamblador compatible con el EMU 8086.
2. Ejecuta el programa y selecciona el archivo de código fuente a ensamblar.
3. El programa realizará las tres fases mencionadas, mostrando mensajes de error o información relevante en cada fase.

Recuerda que este proyecto se centra en las funcionalidades específicas mencionadas y no abarca aspectos adicionales del ensamblador o el EMU 8086. Es importante tener en cuenta las limitaciones y requisitos de sintaxis propios del ensamblador y el procesador objetivo.

¡Disfruta ensamblando tu código con el proyecto EMU 8086 Assembler!
