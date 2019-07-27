from collections import Counter

base_str = "a"


def encode_string(string):
    letters = list(string)
    i = 0
    counter = 1
    res = ""
    while i <= len(letters):
        if i - 1 < 0:
            i += 1
            continue
        if i == len(letters):
            res += letters[i - 1] if counter == 1 else str(counter) + letters[i - 1]
            break
        if letters[i] != letters[i-1]:
            res += letters[i-1] if counter == 1 else str(counter) + letters[i-1]
            counter = 1
        else:
            counter += 1
        i += 1
    print(res)


if __name__ == "__main__":
    encode_string(base_str)