with open("input.txt") as file:
    n, m = map(int, file.readline().split())
    matrix = [list(line.strip()) for line in file]
for i in range(n):
    for j in range(m):
        count = 0
        if matrix[i][j] == ".":
            if i + 1 < n and matrix[i+1][j] == "*":
                count += 1
            if i + 1 < n and j + 1 < m and matrix[i+1][j+1] == "*":
                count += 1
            if j + 1 < m and matrix[i][j+1] == "*":
                count += 1
            if i - 1 >= 0 and j-1 >= 0 and matrix[i-1][j-1] == "*":
                count += 1
            if i - 1 >= 0 and matrix[i-1][j] == "*":
                count += 1
            if j - 1 >= 0 and matrix[i][j-1] == "*":
                count += 1
            if j + 1 < m and i - 1 >= 0 and matrix[i-1][j+1] == "*":
                count += 1
            if i + 1 < n and j - 1 >= 0 and matrix[i+1][j-1] == "*":
                count += 1
            matrix[i][j] = count
for row in matrix:
    for item in row:
        print(item, end="")
    print("\n", end="")