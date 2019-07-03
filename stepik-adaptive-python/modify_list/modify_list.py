lst = [10, 5, 8, 3]


def modify_list(l):
    l[:] = [x//2 for x in l if x % 2 == 0]

modify_list(lst)
print(lst)
