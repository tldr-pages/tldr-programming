# format

> Convert a value to a formatted representation.
> See also: `bin`.
> More information: <https://docs.python.org/3/library/functions.html#format>.

- Convert an integer to binary (base 2):

```python
format(3, "b")
```

- Convert an integer to octal (base 8):

```python
format(9, "o")
```

- Convert an integer to hex (base 16), using lowercase letters for the digits above 9:

```python
format(17, "x")
```

- Convert a float to scientific notation:

```python
format(0.5, "e")
```

- Convert a float to a percentage:

```python
format(3, "%")
```
