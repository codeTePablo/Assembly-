
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
     
stack segment
    dw 0256H dup(0)
ends
     
     
code segment
AAA
AAD 
HLT
INTO 
SCASW
STC
ETIQUETA1: 
DEC DX
IDIV VAR1
IMUL CL
POP [DI+29]
POP [DI]

POP [BX+SI+125]
POP [BX+SI+785]



ETIQUETA2:
ADC VAR2,0FFH
CMP WORD PTR[BX+SI+100],500
LES DX,VAR4
LDS DI,VAR9
ETIQUETA3:
JA ETIQUETA1 
JC ETIQUETA2
JGE ETIQUETA3
JNB ETIQUETA1
JNG ETIQUETA2
JNO ETIQUETA3
ends

 