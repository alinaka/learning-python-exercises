def generate():
    a = 0
    while True:
        a += 1
        for _ in range(a):
            yield a


with open("input.txt") as file:
    number = int(file.read().strip())
gen = generate()
for item in range(number):
    print(next(gen), end=" ")


