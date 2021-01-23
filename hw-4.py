user_str = input('Введине несколько слов через пробел: ')

for i, el in enumerate(user_str.split(' '), 1):
    print(i, el if len(el) < 10 else el[:10])
