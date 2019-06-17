def adder(*args):
    summa = args[0]
    for i in args[1:]:
        summa += i
    return summa


print(adder(1, 3, 1))
print(adder("dfdf"))
print(adder([0, 1], [2, 3]))
