from collections import Counter
from random import randint


def most_frequent(n):
    c = Counter(n).most_common()
    f = c[0][1]
    arr = []
    for k, v in c:
        if v == f:
            arr.append(k)
        else:
            break
    return max(arr)


def main():
    n = int(input())
    k = list(map(int, input().split()))
    assert len(k) == n
    print(most_frequent(k))


def test():
    # k = [3, 3, 3]
    # assert most_frequent(k) == 3
    # k = [4, 1, 4, 3, 3]
    # assert most_frequent(k) == 4
    # k = list(map(int, "10 6 10 10 10 10 8 8 10 9".split()))
    # assert most_frequent(k) == 10
    n = 10**9
    k = (randint(1, 300000) for _ in range(n))
    most_frequent(k)


if __name__ == "__main__":
    test()
