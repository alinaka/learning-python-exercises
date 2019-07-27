from collections import Counter

scores = input().split()
c = Counter(scores)
print(f"{c['A'] / len(scores):.2f}" if "A" in c else "0.00")
