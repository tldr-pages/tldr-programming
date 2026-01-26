# sorted

> Create a new sorted list from an iterable.
> More information: <https://docs.python.org/3/library/functions.html#sorted>.

- Sort an iterable, creating a new list:

```python
sorted({3, 2, 1})
```

- Sort strings as if they were integers:

```python
sorted(["11", "2", "3"], key=int)
```

- Sort strings by length:

```python
sorted(["asdf", "qwerty", "z"], key=len)
```

- Sort in reversed (descending) order:

```python
sorted([1, 2, 3], reverse=True)
```
