from collections import Counter

with open("input.txt") as file:
    numbers = list(map(int, file.read().strip().split()))
c = Counter(numbers)
for key, value in c.items():
    if value > 1:
        print(key, end=" ")