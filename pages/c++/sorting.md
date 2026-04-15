---
keywords: [sort, partition]
---
# sorting

> Sort different elements based on conditions.
> More information: <https://en.cppreference.com/w/cpp/header/algorithm.html>.

### Prerequiresites

```cpp
#import <algorithm>
#include <iterator>
```

- Sort an array:

```cpp
int main()
{
  int array[6] = { 5,9,2,10,1,7 };
  std::sort(std::begin(array), std::end(array), [](int a, int b) {
    return {{condition}};
  });
}
```

- Partition an array into two from a cutoff point:

```cpp
int main()
{
  int array[6] = { 5,9,2,10,1,7 };
  std::partition(std::begin(array), std::end(array), [](int a) {
    return {{condition}};
  });
}

```
