# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import inspect

def stack_depth():
    return len(inspect.getouterframes(inspect.currentframe()))-1

def fibonacci_brute_force(n):

    print("{indent} fibonacci_brute_force({n}) called".format(indent=" "*stack_depth(),n=n))
    if n <= 2:
        return 1
    else:
        return fibonacci_brute_force(n-1) + fibonacci_brute_force(n-2)

def fib_top_down(n):

    print("{indent} fib memo({n})".format(indent=" "*stack_depth(),n=n))
    if n <= 2:
        return 1

    if not hasattr(fib_top_down,'cache'):
        fib_top_down.cache = {}

    if n not in fib_top_down.cache:
            fib_top_down.cache[n]= fib_top_down(n-1) + fib_top_down(n-2)

    return fib_top_down.cache[n]

def cached(f):
    cache={}
    def worker(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return worker

@cached
def fib_with_decorator(n):

    print("{indent} fib memo({n})".format(indent=" "*stack_depth(),n=n))
    if n <= 2:
        return 1

    return fib_with_decorator(n-1) + fib_with_decorator(n-2)

from functools import lru_cache
@lru_cache(maxsize=None)
def fib_with_lru_cache(n):
    if n<=1:
        return 1
    return fib_with_lru_cache(n-1) + fib_with_lru_cache(n-2)

def fib_bottom(n):
    series=[1,1]

    while len(series)<n:
        series.append(series[-1]+series[-2])
    return series[-1]


def fib_bottom_with_o1space(n):
    previous,current =1,1

    for i in range(n-2):
        next = current+previous
        previous,current = current,next

    return current 


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # x = fibonacci_brute_force(6)
    # print(x)
    # y = fib_top_down(6)
    # print(y)
    # y = fib_with_decorator(6)
    # print(y)
    y = fib_with_lru_cache(6)
    print(y)

