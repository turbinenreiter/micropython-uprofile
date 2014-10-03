# uprofile
# uprofile provides a class for simple profiling of functions in micropython.

'''
The MIT License (MIT)

Copyright (c) 2014 Sebastian Plamauer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import pyb

class Profiler():
    '''
    Profiler class to time functions and count how often they get called.
    '''

    results = {}

    @classmethod
    def profile(cls, func):
    '''
    Decorator to wrap the functions to be profiled.
    '''
        cls.results[str(func).split(' ')[1]] = {'dt':[]}
        cls.results[str(func).split(' ')[1]]['order'] = len(cls.results)
        def profiled_func(*args, **kwargs):
            t0 = pyb.micros()
            func_returns = func(*args, **kwargs)
            cls.results[str(func).split(' ')[1]]['dt'].append(pyb.elapsed_micros(t0))
            return func_returns
        return profiled_func

    @classmethod
    def print_results(cls, time_unit='us'):
    '''
    Prints the results of the profiler. Pass us, ms or s to set the time unit.
    '''

        print('\n\tprofiler results\n')

        if time_unit == 'us':
            print('time in microseconds')
            scale = 1
        elif time_unit == 'ms':
            print('time in milliseconds')
            scale = 10**3
        elif time_unit == 's':
            print('time in seconds')
            scale = 10**6
        else:
            print('use us, ms or s, defaulting to ms')
            print('time in microseconds')

        print('')

        names = ('func', 'ncalls', 'tottime', 'percall')
        output = ['']*len(cls.results)
        for key, val in sorted(cls.results.items()):
            ncalls = len(val['dt'])
            tottime = sum(val['dt'])/scale
            percall = tottime/ncalls
            output[val['order']-1] = [key, ncalls, str(tottime)[0:7], percall]

        row_format = '{}\t'*len(names)
        print(row_format.format(*names))
        for line in output:
            print(row_format.format(*line))

        print('')
