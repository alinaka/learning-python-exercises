# plus, minus, multiply, divide

number1, operator, number2 = "13 divide 3".split()
number1, number2 = map(int, (number1, number2))
if operator == 'plus':
    result = number1 + number2
elif operator == 'minus':
    result = number1 - number2
elif operator == 'multiply':
    result = number1 * number2
elif operator == 'divide':
    result = number1 // number2
print(result)