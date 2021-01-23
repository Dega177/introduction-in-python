my_list = [7, 5, 3, 3, 2]

user_input = None

while user_input != 'E':
    user_input = input('Введите число для добавления в рейтинг или "E" для выхода: ')
    if user_input == 'E':
        print('Программа завершена')
        break

    number = int(user_input)

    for el in my_list:
        if number > el:
            my_list.insert(my_list.index(el), number)
            break
    else:
        my_list.append(number)

    print(my_list)
