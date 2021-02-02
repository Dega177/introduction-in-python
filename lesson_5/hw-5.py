from random import randint

with open('text_5.txt', 'w+', encoding='utf-8') as file:
    file.write(' '.join([str(randint(0, 300)) for _ in range(20)]))
    file.seek(0)
    content = file.read()

print(sum([int(num) for num in content.split(' ')]))
