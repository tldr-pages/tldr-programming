# Style guide

This page lists specific formatting instructions for `tldr-programming` pages.

## Contents

1. [General layout](#general-layout)
2. [Directory structure & filenames](#directory-structure--filenames)
3. [Frontmatter & keywords](#frontmatter--keywords)
4. [General writing](#general-writing)
5. [Code blocks](#code-blocks)
6. [Placeholders](#placeholders)

## General layout

The basic format of each page should match the following template:

1.  **YAML Frontmatter**: For search indexing.
2.  **Title**: The name of the topic.
3.  **Description**: Short, snappy description.
4.  **Links**: Link to official documentation.
5.  **Examples**: A list of practical examples.

Template:

````md
---
keywords: [function_name, method_name]
---
# topic

> Short, snappy topic description.
> More information: <https://example.com/documentation>.

- Description of the first example:

```language
code_snippet
```

- Description of the second example:

```language
code_snippet
```
````

Example (`pages/python/file-io.md`):

````md
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

- Read all lines into a list:

```python
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
```
````

## Directory structure & filenames

Files must be grouped by **programming language**.

```text
pages
└ <language>
  ├ hello-world.md
  ├ file-io.md
  ├ concurrency.md
  └ json.md
```

### Topic-based approach

Unlike the original `tldr` project, which maps one page to one command, `tldr-programming` maps one page to a **Topic**.

*   **Do** group related functionality together.
    *   `pages/cpp/stl-algorithms.md` (Covers `sort`, `partition`, `find` in one place).
    *   `pages/python/json.md` (Covers `loads`, `dumps`, `load`, `dump`).
*   **Do not** create tiny pages for single functions.
    *   `pages/cpp/std/sort.md`.
    *   `pages/python/json/dumps.md`.

The goal is to provide a "Cheat Sheet" experience where the user can see related patterns in one context.

## Frontmatter & keywords

To support deterministic search in client, every page **must** start with a YAML frontmatter block containing a `keywords` list.

### Strict keyword rule

To maintain consistency and avoid ambiguity:

1.  `keywords` must contain **only functions or methods** that are **explicitly used** in the code examples.
2.  **Do not** include language keywords (e.g., `with`, `return`, `class`, `import`).
3.  **Do not** include abstract concepts (e.g., `io`, `append`) unless there is an actual method called `.append()` in the code.
4.  **Do not** include parameters (e.g., `encoding`, `mode`).

**Example:**

If the code is:
```python
with open("file.txt", "w") as f:
    f.write("text")
```

*   **Correct keywords:** `[open, write]`
*   **Incorrect keywords:** `[close, with, file, io]` (Implicit or abstract concepts are excluded).

## General writing

### Imperative Mood

- **All descriptions must be phrased in the imperative mood.**
- `Read a file line by line` is preferred instead of `Reading a file line by line`.

### Heading & links

- The page title (`# topic`) must match the filename exactly.
- On the `More information` line, provide a direct link to the **official documentation** (e.g., docs.python.org, cppreference.com, MDN).
- All links must be enclosed inside angular brackets (`<` and `>`).

## Code Blocks

Unlike standard tldr pages, code examples must use **triple backticks** with a **language identifier**.

*   **Correct:**
    ````md
    ```python
    print("Hello")
    ```
    ````
*   **Incorrect:**
    ```md
    `print("Hello")`
    ```
    or
    ````md
    ```
    print("Hello")
    ```
    ````

This is critical for syntax highlighting in client.

## Placeholders

User-provided values should use the `{{placeholder}}` syntax.

*   Use short but descriptive placeholders: `{{filename}}`, `{{key}}`, `{{value}}`.
*   If the placeholder represents a string in the code, keep the quotes **outside** the placeholder if syntax requires it.
    *   *Good:* `print("{{Hello World}}")`
    *   *Bad:* `print({{"Hello World"}})`
    
