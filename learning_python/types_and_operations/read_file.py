# myfile = print(open("myfile.txt").read())

with open("myfile.txt") as myfile:
    print(myfile.read())
