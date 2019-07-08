"""
В римской системе счисления для обозначения чисел используются следующие символы
(справа записаны числа, которым они соответствуют в десятичной системе счисления):

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
Будем использовать вариант, в котором числа 4, 9, 40, 90, 400 и 900 записываются как вычитание
из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.

Напишите программу, которая переводит число из римской в десятичную систему счисления.

Формат ввода:
Строка, содержащая число, закодированное в римской системе счисления. Гарантируется, что число меньше 4000.

Формат вывода:
Строка, содержащая число в десятичной системе счисления, соответствующее введённому.

Sample Input 1:

MCMLXXXIV
Sample Output 1:

1984
Sample Input 2:

IX
Sample Output 2:

9
Sample Input 3:

III
Sample Output 3:

3
"""

string = "MCMLXXXIV"

dictionary = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
curr = result = 0
reversed_string = list(reversed(string))

while curr < len(string):
    if curr + 1 < len(string) and dictionary[reversed_string[curr + 1]] < dictionary[reversed_string[curr]]:
        result += dictionary[reversed_string[curr]] - dictionary[reversed_string[curr + 1]]
        curr += 1
    else:
        result += dictionary[reversed_string[curr]]
    curr += 1
print(result)
