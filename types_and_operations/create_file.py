# myfile = open("myfile.txt", "w")
# myfile.write("Hello file world!\n")
# myfile.close()

with open("myfile.txt", "w") as myfile:
    myfile.write("Hello file world!\n")
