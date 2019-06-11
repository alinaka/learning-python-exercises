import os

result = []
for item in os.walk('sample'):
    for filename in item[2]:
        if filename.endswith('.py'):
            result.append(item[0])
            break
result.sort()
with open('files_answer.txt', 'w') as file:
    file.write('\n'.join(result))
