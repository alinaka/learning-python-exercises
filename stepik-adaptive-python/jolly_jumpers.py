import sys
from typing import List


def is_jolly(array: List[int]) -> bool:
    result = list(map(lambda a, b: abs(a - b), array[1:], array[:-1]))
    if sorted(result) == list(range(1, len(array))):
        return True
    return False


def main():
    array = list(map(int, sys.stdin.read().strip().split()))
    print("Jolly") if is_jolly(array) else print("Not jolly")


if __name__ == "__main__":
    main()
