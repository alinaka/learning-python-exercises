import sys

while True:
    command = sys.stdin.readline().strip()
    if command == "End":
        break
    print(f'Processing "{command}" command...')
print("Good bye!")
