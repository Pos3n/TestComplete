"""A few of math with lists."""

import itertools
import functools

def gfib(c):
    a, b =0, 1
    while a<c:
        yield a
        a, b= b, b+a

if __name__ == "__main__":
    """1. Sum all the natural numbers below one thousand that are multiples of 3 or 5."""
    print(functools.reduce(lambda x, y: x+y , list(filter(lambda x: x%5==0 and x%3==0, [x for x in range(1,1000)]))))



    """2. Calculate the smallest number divisible by each of the numbers 1 to 20."""
    print((list(filter(lambda x: x%2==0 and x%3==0 and x%5==0 and x%7==0 and x%11==0 and x%13==0 and x%17==0 and x%19==0,[x for x in range(1,100000000)])))[0])


    """3. Calculate the sum of the figures of 2^1000"""
    print(functools.reduce(lambda x,y: x+y,[2**x for x in range(1,1001)]))


    """4. Calculate the first term in the Fibonacci sequence to contain 1000 digits """
    print(list(gfib(1000))[0])

