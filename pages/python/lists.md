---
keywords: [append, extend, insert, remove, pop, sort, reverse]
---
# lists

> Manage mutable sequences of elements.
> More information: <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>.

- Add an item to the end of the list:

```python
{{list_name}}.append({{item}})
```

- Extend the list by appending all items from the iterable:

```python
{{list_name}}.extend({{iterable}})
```

- Insert an item at a given position:

```python
{{list_name}}.insert({{index}}, {{item}})
```

- Remove the first item from the list whose value is equal to a specific value:

```python
{{list_name}}.remove({{value}})
```

- Remove and return the item at a given position (defaults to the last item):

```python
{{list_name}}.pop({{index}})
```

- Sort the items of the list in-place:

```python
{{list_name}}.sort()
```

- Reverse the elements of the list in-place:

```python
{{list_name}}.reverse()
```
