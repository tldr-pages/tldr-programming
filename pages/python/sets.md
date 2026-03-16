---
keywords: [set, add]
---
# sets

> Manage mutable, unordered collections of unique elements.
> More information: <https://docs.python.org/3/tutorial/datastructures.html#sets>.

- Create a set (note that an empty set will become a dictionary instead):

```python
{ {{1}}, {{2}}, {{3}} }
```

- Convert an existing iterable (e.g. list) to a set, removing all duplicate values:

```python
set({{iterable}})
```

- Add an element to a set:

```python
{{set1}}.add({{element}})
```

- Keep elements that exist in the first set, but not in the second set:

```python
{{set1}} - {{set2}}
```

- Merge two sets:

```python
{{set1}} | {{set2}}
```

- Keep elements that are in both sets:

```python
{{set1}} & {{set2}}
```

- Keep elements that are in the first or second set, but not both (XOR):

```python
{{set1}} ^ {{set2}}
```
