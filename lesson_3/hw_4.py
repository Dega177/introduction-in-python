def involution(x, y):
    for i in range(1, abs(y)):
        x *= x
    return abs(1 / x)


number_1 = 0
while number_1 <= 0:
    number_1 = input('Введите действительное положительное число: ')
    try:
        number_1 = float(number_1)
        if number_1 <= 0:
            print('Число должно быть больше 0!')
    except ValueError:
        print('Необходимо ввести число!')
        number_1 = 0

number_2 = 0
while number_2 >= 0:
    number_2 = input('Введите целое отрицательное число: ')
    if '.' in number_2:
        print('Число должно быть целым отрицательным!')
        number_2 = 0
    else:
        try:
            number_2 = int(number_2)
            if number_2 >= 0:
                print('Число должно быть меньше 0!')
        except ValueError:
            print('Необходимо ввести число!')
            number_2 = 0

print(f'Число {number_1} в степени {number_2}: {involution(number_1, number_2):.05f}')
