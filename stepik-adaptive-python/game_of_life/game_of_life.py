with open("input.txt") as file:
    n, m = map(int, file.readline().split())
    board = [list(file.readline().strip()) for _ in range(n)]

overall = []
for i in range(n):
    result = []
    for j in range(m):
        alive = 0
        if board[i - 1][j - 1] == "X":
            alive += 1
        if board[i - 1][j] == "X":
            alive += 1
        if board[i][j - 1] == "X":
            alive += 1
        if j + 1 < m:
            if board[i - 1][j + 1] == "X":
                alive += 1
            if board[i][j + 1] == "X":
                alive += 1
        else:
            if board[i - 1][0] == "X":
                alive += 1
            if board[i][0] == "X":
                alive += 1
        if i + 1 < n:
            if board[i + 1][j - 1] == "X":
                alive += 1
            if board[i + 1][j] == "X":
                alive += 1
        else:
            if board[0][j - 1] == "X":
                alive += 1
            if board[0][j] == "X":
                alive += 1
        if j + 1 < m and i + 1 < n:
            if board[i + 1][j + 1] == "X":
                alive += 1
        elif i + 1 < n:
            if board[i + 1][0] == "X":
                alive += 1
        elif j + 1 < m:
            if board[0][j + 1] == "X":
                alive += 1
        else:
            if board[0][0] == "X":
                alive += 1
        if alive == 3 and board[i][j] == ".":
            result.append("X")
        elif alive != 2 and alive != 3 and board[i][j] == "X":
            result.append(".")
        else:
            result.append(board[i][j])
    overall.append(result)
for item in overall:
    print(*item, sep="")
