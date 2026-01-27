> Sort array elements before and after a condition
> More information: <https://en.cppreference.com/w/cpp/algorithm/partition>

- Partition an array:

```
std::partition(array.begin(), array.end(), [](const {{int}}) &a) {
  return {{condition}}
}
```
