with open("input.txt") as f:
    size = int(f.read())
result = [[i for i in range(size)] for i in range(size)]
numbers = [i for i in range(1, size**2 + 1)]
result[0] = numbers[:size]
counter = n = size
times = 0
row, col = 0, size - 1
for _ in range(1, n):
    if times % 2 == 0:
        for _ in range(1, n):
            row += 1
            result[row][col] = numbers[counter]
            counter += 1
        for _ in range(1, n):
            col -= 1
            result[row][col] = numbers[counter]
            counter += 1
    else:
        for _ in range(1, n):
            row -= 1
            result[row][col] = numbers[counter]
            counter += 1
        for _ in range(1, n):
            col += 1
            result[row][col] = numbers[counter]
            counter += 1
    times += 1
    n -= 1
for i in result:
    for j in i:
        print(j, end=' ')
    print('')
