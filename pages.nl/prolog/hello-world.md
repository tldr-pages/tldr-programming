# hello-world

> Basissyntax voor het tonen van tekst naar de standaarduitvoer.
> Meer informatie: <https://www.swi-prolog.org/pldoc/doc_for?object=write/1>.

- Toon een eenvoudige tekenreeks met een nieuwe regel:

```prolog
:- initialization(main).

main :-
    write('Hello World'), nl,
    halt.
```
