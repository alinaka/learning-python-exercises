"""
Арбузы
(Время: 0,5 сек. Память: 16 Мб Сложность: 14%)
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!

Входные данные
В первой строке входного файла INPUT.TXT задано одно число N – количество арбузов.
Вторая строка содержит N чисел, записанных через пробел.
Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

Выходные данные
В выходной файл OUTPUT.TXT нужно вывести два числа через пробел:
массу арбуза, который Иван Васильевич купит теще и массу арбуза, который он купит себе.
"""
from random import randint


def get_min_and_max(numbers):
    return map(str, (min(numbers), max(numbers)))


def main():
    with open("input.txt") as file:
        n = int(file.readline().strip())
        numbers = list(map(int, file.readline().strip().split()))

    with open("output.txt", "w") as file:
        file.write(" ".join(get_min_and_max(numbers)))


def test():
    for _ in range(50):
        n = randint(1, 30000)
        numbers = [randint(1, 30000) for _ in range(n)]
        a, b = get_min_and_max(numbers)
        assert a == str(min(numbers))
        assert b == str(max(numbers))


if __name__ == "__main__":
    main()
