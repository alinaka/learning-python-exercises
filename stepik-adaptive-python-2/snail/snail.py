"""
Snail

Snail creeps up the vertical pole of height H feets.
Per day it goes A feets up, and per night it goes B feets down.
In which day the snail will reach the top of the pole?

Input data format

On the input the program receives non-negative integers H, A, B, where H > B and A > B. Every integer does not exceed 100.

Sample Input:

10
3
2
Sample Output:

8
"""

def snail(H, A, B):
    day = 0
    current = 0
    while current < H:
        current += A - B
        day += 1
    return day


def main():
    H, A, B = map(int, [input() for _ in range(3)])
    print(snail(H, A, B))


def test():
    assert snail(10, 3, 2) == 8


if __name__ == "__main__":
    test()
