input_information = [
    'Иванов 10000.0',
    'Петров 15000.0',
    'Сидоров 25000.1',
    'Иванова 15000.7',
    'Петрова 19000.9',
    'Сидорова 26000.1',
    'Октябрьский 30000.5',
    'Петровский 26000.4',
    'Знаменский 12000.0',
    'Корецкий 31000.9'
]

with open('text_3.txt', 'a+', encoding='utf-8') as file:
    file.writelines(line + '\n' for line in input_information)
    file.seek(0)
    content = file.readlines()

employees_info = {}
for employee in content:
    name, salary = employee.split(' ')
    employees_info[name] = float(salary)

print(f'Зарабатывают менее 20 000: '
      f'{[name for name, salary in employees_info.items() if salary < 20000]}')
print(f'Средний заработок: {float(sum(employees_info.values()) / len(employees_info.values())):.2f}')
