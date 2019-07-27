def main():
    with open("input.txt") as file:
        first = file.readline().strip().lower()
        second = file.readline().strip().lower()
    print(sorted(first) == sorted(second))


if __name__ == "__main__":
    main()
