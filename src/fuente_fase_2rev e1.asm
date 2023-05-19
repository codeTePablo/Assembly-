     
stack segment
    dw 256 dup(0)
ends
data segment
    var1 db 0

    var2 db "hola de nuevo$"
    var3 db CX
    var4 db 10 dup('A')
    var5 db 1000
    var6 db 30 dup(100)
    var7 dw 600
    var8 dw 100000
    var9 dw 20 dup (700)
    var10 dw 023456H
    const1 equ 23
    const2 equ 4000000
    var11 dw 050H 
    VAR7 db 11           
ends
     
     
code segment
AAA 010H
ETIQUETA1: 
AAD
SCASW
AAD 
HLT DI
dsfsdfs
INTO 
SCASW VAR6
DEC VAR7
STC
DEC DX,SI
IDIV VAR1
IMUL CON1
POP CX
ETIQUETA2:

ADC VAR2,0FFFH
CMP WORD PTR[BX+SI+100],500
LES VAR6
LDS DX,VAR3

ETIQUETA3:

JA 
JC ETIQUETA3
JGE VAR4
JNB ETIQUETA2
JNG 10
JNO ETIQUETA1
MOV VAR3,DH
ends

 