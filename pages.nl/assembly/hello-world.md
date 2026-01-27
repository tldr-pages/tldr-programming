# hello-world

> Basissyntax voor het tonen van tekst naar de standaarduitvoer (x86_64 Linux via syscalls).
> Meer informatie: <https://www.nasm.us/doc/nasm03.html>.

- Toon een eenvoudige tekenreeks met de sys_write syscall:

```nasm
section .data
    msg db "Hello World", 0xA
    len equ $ - msg

section .text
    global _start

_start:
    ; sys_write(stdout, msg, len)
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    ; sys_exit(0)
    mov rax, 60
    mov rdi, 0
    syscall
```
