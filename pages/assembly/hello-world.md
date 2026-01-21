# hello-world

> Basic syntax for printing text to standard output (x86_64 Linux via syscalls).
> More information: <https://www.nasm.us/doc/nasm03.html>.

- Print a simple string using the sys_write syscall:

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
