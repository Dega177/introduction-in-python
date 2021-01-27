user_input = None
total_sum = 0

while user_input != 'Q':

    user_input = input('Введите числа, разделенные пробелами или "Q" для выхода: ').split()

    numbers = [float(el) for el in user_input if not el.isalpha()]
    user_input = [el.upper() for el in user_input if el.isalpha()]

    if 'Q' in user_input:
        user_input = 'Q'
    elif user_input:
        print('Можно вводить только числа или "Q". Будте внимательнее!')

    sum_of_iteration = sum(numbers)
    total_sum += sum_of_iteration

    print(f'Сумма этапа: {sum_of_iteration}\n'
          f'Общая сумма: {total_sum}')
else:
    print('Программа завершена')
