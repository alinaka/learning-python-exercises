def getCamelCase(string_with_underscore):
    return string_with_underscore.title().replace("_", "")


def main():
    string = input().strip()
    print(getCamelCase(string))


if __name__ == "__main__":
    main()
