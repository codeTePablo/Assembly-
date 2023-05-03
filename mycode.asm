data segment
    var1 db "a"
    var2 dw -32770
    estesi dw -32769
    var2 db  255 
    pkey db "press any key...$"
    var dw 65536
    var db "ala"
    var2 db 255
    estenodeberia db 256
    prueb EQU 100

    6587 var 2
    db orp 87
    
    prueba equ 100
    var dw DUP (100)
    dw 100 dup (0)
ends

stack segment
    dw   65535  dup(0)
ends

code segment
start:
    mov ax, data
    mov ds, ax
    mov es, ax
    
    inic io:
    fin:
    etiq1:
    etiq 2:
    9878etique:

    DEC AX 
    IDIV BX
    IMUL CX
    ADC AX, BX
    CMP CX, DX
    LES AX, [BX]
    LES [BX]
    LDS AX, [SI]

    lea dx, pkey
    mov ah, 9
    int 21h        
    
    mov ah, 1
    int 21h
    
    mov ax, 4c00h 
    int 21h    
ends

end start 