# Style Guide

## Directory Structure

Files should be grouped by programming language.

```
pages
└ <language>
  ├ hello-world.md
  ├ file-io.md
  └ concurrency.md
```

## Page Format

Each page must follow this format:

1.  **Title:** The name of the concept or function (h1 header).
2.  **Description:** A short explanation of what this code does (blockquote).
3.  **More information:** A link to the official documentation (blockquote).
4.  **Examples:** A list of examples with descriptions.
5.  **Code blocks:** Must use triple backticks with the **language identifier** (e.g., `python`, `rust`, `cpp`) to enable syntax highlighting in clients.

### Example Template

````md
# <topic>

> <Short description>.
> More information: <https://official-docs.url>.

- <Example description>:

```<language>
<code snippet>
```
````
