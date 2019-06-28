def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        try:
            x = int(input())
        except ValueError:
            print(error_message)
        else:
            print(end_message)
            return x


if __name__ == "__main__":
    x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
