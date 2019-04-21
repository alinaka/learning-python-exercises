D = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7}

keys_list = list(D.keys())
keys_list.sort()
for key in keys_list:
    print(key, "=>", D[key])

for key in sorted(D):
    print(key, "=>", D[key])
