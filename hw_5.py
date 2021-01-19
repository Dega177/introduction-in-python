earnings = int(input('Введите выручку вашей фирмы: '))
cost = int(input('Введите расходы вашей фирмы: '))

if earnings > cost:
    profitability = (earnings - cost) / earnings
    print(f'Вы получили прибыль\nРентабельность – {profitability:.2%}')
elif earnings == cost:
    print('Вы работаете в 0')
else:
    print('Вы получили убыток')

number_of_employees = int(input('Введите количество сотрудников: '))
profit_per_employees = (earnings - cost) / number_of_employees
print(f'Прибыль на одного сотрудника: {profit_per_employees:.2f}')
