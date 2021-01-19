my_int = 11
print(my_int)

my_float = 3.45
print(my_float)

my_str = 'Some text'
print(my_str)

my_list = [2, 3, 5, 7, 2.34, 'text']
print(my_list)

my_dict = {'name': 'Раф', 'breed': 'spaniel', 'age': 10, 'gender': 'M'}
print(my_dict)

city = input('Введите город, в котором вы живете: ')
population = int(input('Введите количество житежелей города: '))
print(f'Вы живете в городе {city}. В этом городе живет еще {population - 1:,} человек.')
