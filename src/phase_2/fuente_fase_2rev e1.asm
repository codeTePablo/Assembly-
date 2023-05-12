stack segment
    dw 0256H dup(0)
ends

data segment
    var999999999999 db 10	   ;ERROR
    var1 db 10101010B             
    var2 db "Ensamblador"
    var3 db 0ABCH              ;ERROR
    var4 dw 0F300H          
    var5 db 30 dup('$')      
    var6 dw                    ;ERROR
    var7 dw 600000             ;ERROR
    var8 dw 1010B dup(056H)
    var9 db 0FF00H dup(100)
    var10 db 10 dup(0000B)
    var11 dw 2000 dup(0AABBCCH);ERROR
    con1 equ 100000            ;ERROR
    con2 equ 800             
ends

code segment
AAA 010H
AAD 
HLT DI
INTO 
SCASW VAR6
STC
ETIQUETA1: 
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

 