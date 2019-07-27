cache = {}
import sys

def sequence(k):
    if k not in cache:
        cache[k] = k if k <= 2 else sequence(k - 1) + sequence(k - 3)
    return cache[k]


def main():
    n = sys.stdin.readline()
    k = map(int, sys.stdin.readline().split())
    # k = range(5)
    print(*(sequence(i) for i in k))


if __name__ == "__main__":
    main()
