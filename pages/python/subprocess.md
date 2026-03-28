---
keywords: [run]
---
# subprocess

> Launch subprocesses from Python.
> More information: <https://docs.python.org/3/library/subprocess.html>.

### Prerequisites

```python
import subprocess
```

- Run a subprocess:

```python
subprocess.run(["{{program}}", {{"argument1", "argument2", ...}}])
```

- Run a subprocess with shell features (pipes, wildcards, etc):

```python
subprocess.run("{{command}}", shell=True)
```
