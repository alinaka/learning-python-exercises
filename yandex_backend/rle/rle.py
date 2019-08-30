def main():
    with open("input.txt") as file:
        decoded = list(file.read().strip())
    result = []
    prev = ''
    curr = ''

    for i, item in enumerate(decoded):
        if not item.isdigit():
            if prev:
                result.append(prev + curr)
                curr = ""
            prev = item
        else:
            curr += item
        if i == len(decoded) - 1:
            result.append(prev + curr)

    count = 0
    for item in result:
        if len(item) == 1:
            count += 1
        else:
            count += int(item[1:])
    with open("output.txt", "w") as file:
        file.write(str(count))

if __name__ == "__main__":
    main()

