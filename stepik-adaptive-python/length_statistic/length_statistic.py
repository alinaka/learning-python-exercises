def main():
    with open("input.txt") as file:
        text = file.readline().strip().split()
    result = {len(i): 0 for i in text}
    for item in text:
        result[len(item)] += 1
    for i in sorted(result):
        print(i, ':', result[i])


def coll():
    import collections
    counter = collections.Counter([len(i) for i in input().split()])
    print(*[f"{x}: {y}" for x, y in sorted(counter.items())], sep='\n')


if __name__ == "__main__":
    coll()
