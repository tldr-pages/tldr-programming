---
keywords: [open, read, write, readlines]
---
# file-io

> Reading and writing files using context managers.
> More information: <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>.

- Read a file line by line (memory efficient):

```python
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)
```

- Write a string to a file (overwriting):

```python
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello World\n")
```

- Append text to the end of a file:

```python
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("Appended text\n")
```

- Read all lines into a list:

```python
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
```

- Read the entire file content into a string:

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```
