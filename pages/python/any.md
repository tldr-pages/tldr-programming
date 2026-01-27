# any

> Return `True` if any element of an iterable is truthy.
> Note: Returns `False` if the iterable is empty.
> More information: <https://docs.python.org/3/library/functions.html#any>.

- Check if any value in an iterable is `True`:

```python
any([False, True, False])
```

- Check if any value in an iterable is non-zero:

```python
any([0, 0, 3, 0])
```

- Check whether any value satisfy a certain condition:

```python
any(number < 0 for number in [-1, 2, 3])
```
