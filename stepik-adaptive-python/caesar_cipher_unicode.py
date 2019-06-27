def get_caesar_cipher(alphabet:str, string: str, offset: int) -> str:
    offset %= len(alphabet)
    alphabet *= 2
    return ''.join([alphabet[alphabet.index(i)+offset] for i in string])


def main():
    alphabet = ''.join([chr(i) for i in range(int(0x1f600), int(0x1f64f)+1)])
    offset = int(input())
    secret = input().strip()
    print(f'Result: "{get_caesar_cipher(alphabet, secret, offset)}"')


if __name__ == "__main__":
    main()
