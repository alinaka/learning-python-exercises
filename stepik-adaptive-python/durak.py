# A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds,
# hearts, or spades (denoted C, D, H, S).
# Each card also has a value of either 6 through 10, jack, queen, king, or ace (denoted 6, 7, 8, 9, 10, J, Q, K, A).
# For scoring purposes card values are ordered as above, with 6 having the lowest and ace the highest value.
#
# Напишите программу, которая определяет, бьёт ли одна карта другую.
# Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
# Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
# Если карты разных мастей и нет козырных, то никто не побеждает.
#
# Формат ввода:
# На первой строке через пробел указываются две карты в формате <значение><масть>,
# а на следующей строке указывается козырная масть.
#
# Формат вывода:
# Программа должна вывести слово
# First, если первая карта бьёт вторую,
# Second, если вторая карта бьёт первую,
# Error, если ни одна из карт не может побить другую.

card1, card2 = input().strip().split()
bonus = input().strip()
card_values = ["6", "7", "8", "9", "1", "J", "Q", "K", "A"]

if card1[-1] == card2[-1]:
    print("First") if card_values.index(card1[0]) > card_values.index(card2[0]) else print("Second")
else:
    if bonus == card1[-1]:
        print("First")
    elif bonus == card2[-1]:
        print("Second")
    else:
        print("Error")

