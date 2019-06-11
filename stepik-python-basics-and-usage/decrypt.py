import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt") as file:
    passwords = file.read().strip().split()

for password in passwords:
    try:
        print(simplecrypt.decrypt(password, encrypted))
    except simplecrypt.DecryptionException:
        pass
