with open("input.txt") as file:
    decoded = list(file.read().strip())
result = []
prev = ''
for item in decoded:
    prev += item
    if not item.isdigit():
        result.append(prev)
        prev = ''
for item in result:
    if len(item) == 1:
        print(item, end="")
    else:
        times = int(item[:-1])
        print(times * item[-1], end="")
