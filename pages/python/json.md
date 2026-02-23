---
keywords: [dumps, dump, loads, load, open]
---
# json

> Encode and decode JSON data.
> More information: <https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json>.

- Parse a JSON string into a Python object:

```python
import json
{{data}} = json.loads("{{json_string}}")
```

- Read JSON data from a text file:

```python
import json
with open("{{file.json}}", "r", encoding="utf-8") as f:
    {{data}} = json.load(f)
```

- Convert a Python object (e.g. dictionary or list) into a JSON string:

```python
import json
json.dumps({{object}})
```

- Write a Python object to a text file as JSON:

```python
import json
with open("{{file.json}}", "w", encoding="utf-8") as f:
    json.dump({{object}}, f)
```
