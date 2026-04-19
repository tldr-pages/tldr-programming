---
keywords: [sort, partition, begin, end]
---
# sorting

> Sort different elements based on conditions.
> More information: <https://en.cppreference.com/w/cpp/header/algorithm.html>.

### Prerequisites

```cpp
#include <algorithm>
#include <iterator>
```

- Sort an array from smallest to biggest:

```cpp
int main()
{
  int array[] = { 5,9,2,10,1,7 };
  std::sort(std::begin(array), std::end(array), [](int a, int b) {
    return {{a < b}};
  });
}
```

- Partition an array into two with smaller in front and with 6 being the cutoff point:

```cpp
int main()
{
  int array[] = { 5,9,2,10,1,7 };
  std::partition(std::begin(array), std::end(array), [](int a) {
    return {{a < 6}};
  });
}
```
