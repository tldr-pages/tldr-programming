# all

> Return `True` if all elements of an iterable are truthy, or the iterable is empty.
> More information: <https://docs.python.org/3/library/functions.html#all>.

- Check if all values in an iterable are `True`:

```python
all([True, True, True])
```

- Check if all values in an iterable are non-zero:

```python
all([1, 2, 3, 4])
```

- Check whether all values satisfy a certain condition:

```python
all(number < 0 for number in [-1, -2, -3])
```
