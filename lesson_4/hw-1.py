from sys import argv
from input_check import is_number

try:
    productivity, rate, premium = argv[1:]

    if is_number([productivity, rate, premium], 'float'):
        productivity, rate, premium = map(float, [productivity, rate, premium])
        print(f'Заработная плата сотрудника: {(productivity * rate) + premium}')
    else:
        print('Проверьте значения. В качестве аргументов принимаются только числа')

except ValueError:
    print(f'Необходимо ввести 3 параметра, а вы ввели {len(argv) - 1}')
