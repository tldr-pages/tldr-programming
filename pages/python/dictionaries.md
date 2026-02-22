---
keywords: [dict, get, list, sorted]
---
# dictionaries

> Manage data stored as key-value pairs.
> More information: <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>.

- Create a dictionary using keyword arguments:

```python
dict({{key1}}={{value1}}, {{key2}}={{value2}}, ...)
```

- Add or update a value for a specific key:

```python
{{dict_name}}["{{key}}"] = {{value}}
```

- Extract a value safely with a default fallback if the key does not exist:

```python
{{dict_name}}.get("{{key}}", "{{default_value}}")
```

- Delete a key-value pair:

```python
del {{dict_name}}["{{key}}"]
```

- Check whether a specific key exists in the dictionary:

```python
"{{key}}" in {{dict_name}}
```

- Get a list of all keys in insertion order:

```python
list({{dict_name}})
```

- Get a sorted list of all keys:

```python
sorted({{dict_name}})
```

- Create a dictionary from a sequence of key-value tuples:

```python
dict([("{{key1}}", {{value1}}), ("{{key2}}", {{value2}}), ...])
```
