from codeSegementlines import *
from functions import *

labels = []


def analizeCodeSegment(
    codeSegment, tuplaNombreVariables8bits, tuplaNombresVariables16bits, variables8bits, variables16bits ,n, count
):
    """
    Esta funcion analiza el segmento de codigo llamando a funciones 
    que analizan cada tipo de instruccion
    """
    print(f"{n+1} -  {format(count, 'x').zfill(4).upper()}H - code segment :linea correcta")
    count = count - count
    for n, line in enumerate(codeSegment, start=n + 2):

        if line.startswith(instrucciones_sin_operando):
            line = cleanLine(line)
            try:
                count = checkLinewithoutOperands(line, n, count)
            except:
                print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} ::no fue posible analizar la linea ")
                
            
        elif line.startswith(instrucciones_con_un_operando):
            try:
                bool, count = analyzeOneOperandCodeSegments(
                    line, tuplaNombreVariables8bits, tuplaNombresVariables16bits,variables8bits, variables16bits, n, count
                )
            except:
                print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :no fue posible analizar la linea")

        elif line.startswith(instruccionconDosOperandos):
                try:
                    bool, count = analyzeTwoOperandsCodeSegments(
                        line, tuplaNombreVariables8bits, tuplaNombresVariables16bits, variables8bits, variables16bits,n, count
                    )
                except:
                    print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :no fue posible analizar la linea")
         
        elif line.startswith(instrucciones_con_operandos):
            try:
                count = analyzeOperandsCodeSegments(
                    line, tuplaNombreVariables8bits, tuplaNombresVariables16bits, n, count, variables8bits, variables16bits
            )
            except:
                print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :no fue posible analizar la linea")
        elif line.startswith(instrucciondeSaltos):
            try:
                count = analyceJumps(
                line,
                n,
                labels,
                tuplaNombreVariables8bits,
                tuplaNombresVariables16bits,
                count,
                )
            except:
                print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :no fue posible analizar la linea")
        elif line.endswith(":"):
            if (CheckingEtiqueta(line,count,  n, line)) == True:
                line = line.replace(":", "")
                result = line + " " + format(count, 'x').zfill(4).upper() 
                result = result.split(" ")
                labels.append(result)
            else:
                pass
            
        elif line.startswith(OtrasInstrucciones):
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} :insturccion no asignada")
        elif line.startswith(numbers):
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} error: simbolo no definido")
        else:
            print(f"{n} -  {format(count, 'x').zfill(4).upper()}H - {line} es un linea incorrecta")
    print(f"{n+1} -  {format(count, 'x').zfill(4).upper()}H - ends :linea correcta")
    return count
