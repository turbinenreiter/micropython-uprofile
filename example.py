from uprofile import Profiler

@Profiler.profile
def fun1(inp1):
    pyb.delay(10)
    return inp1**10

@Profiler.profile
def fun2(inp2):
    if type(inp2) is int:
        return inp2%2
    else:
        print('not an int')
        return None

@Profiler.profile
def fun3(inp):
    for i in range(inp):
        print(fun1(i))
        print(fun2(i))
    fun2('str')

def res():
    Profiler.print_results(time_unit='s')

fun3(128)
