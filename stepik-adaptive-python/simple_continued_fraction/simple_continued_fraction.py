import sys

a, b = map(int, sys.stdin.readline().split("/"))

res = []
while b != 0:
    res.append(a // b)
    a, b = b, a % b
print(*res)
