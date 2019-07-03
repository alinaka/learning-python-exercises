def main():
    with open("input.txt") as file:
        numbers = file.readline().split()
        number = file.readline().strip()
    print(*[i for i, item in enumerate(numbers) if item == number] or [None])


if __name__ == "__main__":
    main()
