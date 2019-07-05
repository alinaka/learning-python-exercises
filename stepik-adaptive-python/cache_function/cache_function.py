import sys

from functools import lru_cache

n = sys.stdin.readline()


@lru_cache()
def func(n):
    return f(n)


for number in map(int, sys.stdin.read().split()):
    print(func(number))
