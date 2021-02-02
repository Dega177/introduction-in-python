import re

with open('text_6.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

lessons = {}
for line in content:
    k, v = line.split(':')
    lessons[k] = sum(list(map(int, re.findall(r'\d+', v))))

print(lessons)
