micropython-uprofile
====================

uprofile provides a class for simple profiling of functions in micropython.

### Quickstart

Example:
```python
from uprofile import Profiler

@Profiler.profile
def fun1(inp1):
    return inp1**10

fun1(10)

Profiler.print_results(time_unit='s')
```
