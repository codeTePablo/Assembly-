data segment
    var11111111111 db 10
    var1 db 10101010B             
    var2 db "Hola"  
    var3 db 0ADAH                                    
    var4 dw 0F800H                        
    var5 db 50 dup(' ')      
    var6 dw                  
    var7 dw 700000           
    var8 dw 0101B dup(034H)
    var9 db 0FF00H dup(120) 
    var10 db 30 dup(0000B)
    var11 dw 3000 dup(022) 
    const1 equ 800000                    
    const2 equ 900                       
ends                                     
stack segment                                  
    dw 0128H dup(100)                    
ends                                      
code segment                                    
HLT AX
HLT
    etiq1:
    etiq2:


    eti q4:
LAHF 0DEH                
STOSB [DS]              
AAA 101010B,200          


    etiq3:
MUL var3                 
PUSH DX,[BX+SI+100]      
IMUL WORD PTR ETIQ3
etiq2:     
RCL ETIQ1                
MOV                     
POPA 20                          
JAE DX,CX                
ETIQ1: JNLE              
JNA                     
LES SI                   
ADD 10101010B           
DIV var5,[BX+500]  
DAS
AAD 
INTO ser, wer
SCASW
STC


IDIV
    IMUL
POP
    ADC
    CMP
    LES
LDS
    JA
    JC
    JGE
    JNB
    JNG
    JNO
 AAM  
    CLI

    CWD

    MOVSB
ends


