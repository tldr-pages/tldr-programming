---
keywords: [execlp, execvp, execve, perror, _exit, fork, waitpid]
---
# exec

> Replace the current process image with a new program.
> Functions only return on error, with `-1` and `errno` set.
> More information: <https://man7.org/linux/man-pages/man3/exec.3.html>.

### Prerequisites

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
```

- Run a program in a child process, report a failure and wait for it to finish:

```c
pid_t pid = fork();
if (pid == 0) {
    execlp("{{ls}}", "{{ls}}", "{{-l}}", NULL);
    perror("execlp");
    _exit(127);
}
waitpid(pid, NULL, 0);
```

- Run a program by its full path, passing arguments as a `NULL`-terminated list (`argv[0]` is the program name):

```c
// int execl(const char *path, const char *arg0, ..., (char *)NULL);
execl("{{/bin/ls}}", "{{ls}}", "{{-l}}", NULL);
```

- Run a program searching `$PATH`, passing arguments as a `NULL`-terminated array:

```c
// int execvp(const char *file, char *const argv[]);
char *args[] = {"{{ls}}", "{{-l}}", NULL};
execvp(args[0], args);
```

- Run a program by its full path with a custom environment:

```c
// int execve(const char *path, char *const argv[], char *const envp[]);
char *args[] = {"{{env}}", NULL};
char *env[] = {"{{VAR=value}}", NULL};
execve("{{/usr/bin/env}}", args, env);
```


