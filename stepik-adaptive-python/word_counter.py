from unittest import mock


def count_words():
    words = input().lower().split()
    for i in set(words): print(i, words.count(i))


def test():
    test_str = "a aa abC aa ac abc bcd a"
    with mock.patch('builtins.input', return_value=test_str):
        dictionary = count_words()


if __name__ == "__main__":
    test()