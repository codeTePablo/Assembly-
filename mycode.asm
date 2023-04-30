data segment
    pkey db "press any key...$"
    var dw 0
    var db "ala"
    var2 db 0
    prueb EQU 100
    prueba equ 100
ends

stack segment
    dw   128  dup(0)
ends

code segment
start:
    mov ax, data
    mov ds, ax
    mov es, ax
    lea dx, pkey
    mov ah, 9
    int 21h        
    mov ah, 1
    int 21h
    mov ax, 4c00h 
    int 21h    
ends

end start 