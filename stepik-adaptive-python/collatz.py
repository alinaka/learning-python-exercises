def get_collatz(n):
    while n != 1:
        yield n
        n = int(n/2) if n % 2 == 0 else n * 3 + 1
    yield n


if __name__ == "__main__":
    n = int(input())
    for i in get_collatz(n): print(i, end=" ")