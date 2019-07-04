dictionary = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}
string = "1984"
number = int(string)

values = {
    1000: number//1000,
    100: (number - number//1000 * 1000)//100,
    10: ((number - number//1000 * 1000) - ((number - number//1000 * 1000)//100*100)) // 10,
    1: number % 10
}

res = ""

for k, v in values.items():
    if v > 0:
        if k == 1000:
            res += v * dictionary.get(k)
        else:
            if v == 4:
                res += dictionary.get(k) + dictionary.get(5*k)
            elif v == 9:
                res += dictionary.get(k) + dictionary.get(10*k)
            else:
                res += v // 5 * dictionary.get(5*k) + (v - v // 5 * 5) * dictionary.get(k)
print(res)
