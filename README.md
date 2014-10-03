micropython-uprofile
====================

uprofile provides a class for simple profiling of functions in micropython.

### Quickstart

1. Import the Profiler class from uprofile.
2. Decorate the function you want to profile with the profile decorator.
3. Run your program.
4. Print the results.

Example:
```python
from uprofile import Profiler            # 1.

@Profiler.profile                        # 2.
def fun1(inp1):
    return inp1**10

fun1(10)                                 # 3.

Profiler.print_results(time_unit='s')    # 4.
```

``Profiler.results`` contains a dictonary, that holds a list of the execution times for each time the function ran.
  
  
**NOTE**  
This needs micropython v1.3.3 on the pyboard.
