S = input()
sum = 0
for char in S:
    print(ord(char))

for char in S:
    sum += ord(char)
print(sum)

print([ord(char) for char in S])
print(list(map(ord, S)))
