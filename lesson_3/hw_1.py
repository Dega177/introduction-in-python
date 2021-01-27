def my_func(a, b):
    return a / b


a = float(input('Введите делимое: '))
b = float(input('Введите делитель: '))

try:
    print(f'Результат деления: {my_func(a, b)}')
except ZeroDivisionError:
    print(f'Делимое не может быть нулем')
