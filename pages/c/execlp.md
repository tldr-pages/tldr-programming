---
keywords: [execlp, perror, _exit, fork, waitpid]
---
# execlp

> Replace the current process image with a new program.
> More information: <https://man7.org/linux/man-pages/man3/exec.3.html>.

| Function | Arguments | Searches `PATH` | Environment |
| --- | --- | --- | --- |
| execl | list | no | inherited |
| **execlp** | **list** | **yes** | **inherited** |
| execle | list | no | `envp` |
| execv | array | no | inherited |
| execvp | array | yes | inherited |
| execve | array | no | `envp` |
| execvpe | array | yes | `envp` (GNU) |

### Prerequisites

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
```

- Run a program found in `PATH` in a child process (repeat the name as `argv[0]`, end with `NULL`) and wait for it:

```c
pid_t pid = fork();
if (pid == 0) {
    execlp("{{ls}}", "{{ls}}", "{{-l}}", NULL);
    perror("execlp");
    _exit(127);
}
waitpid(pid, NULL, 0);
```
