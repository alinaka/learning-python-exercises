example = "abc"
substr = "d"
index = 0
if substr not in example:
    print(-1)
else:
    while index < len(example):
        index = example.find(substr, index)
        if index == -1:
            break
        print(index, end=" ")
        index += 1
