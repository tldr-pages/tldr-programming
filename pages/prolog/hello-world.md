# hello-world

> Basic syntax for printing text to standard output.
> More information: <https://www.swi-prolog.org/pldoc/doc_for?object=write/1>.

- Print a simple string and newline:

```prolog
:- initialization(main).

main :-
    write('Hello World'), nl,
    halt.
```
