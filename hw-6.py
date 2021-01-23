products = []
product_analytics = {'Название': [],
                     'Цена': [],
                     'Количество': [],
                     'Ед': []}
products_count = 1
user_input = '1'

while user_input != '4':
    if user_input == '1':
        name = input('Введите название товара: ')
        price = input('Введите цену товара: ')
        amount = input('Введите количество товара: ')
        measure = input('Введите единицу измерения: ')

        product_analytics['Название'].append(name)
        product_analytics['Цена'].append(price)
        product_analytics['Количество'].append(amount)
        product_analytics['Ед'].append(measure)

        products.append((products_count, {'Название': name, 'Цена': price, 'Количество': amount, 'Ед': measure}))

        products_count += 1
    elif user_input == '2':
        print('Список добавленных товаров:')
        for el in products:
            print(el)
    elif user_input == '3':
        print('Товарная аналитика:')
        for k, v in product_analytics.items():
            print(f'{k}: {list(set(v))}')

    user_input = input('Введите число, чтобы выбрать следующее действие:\n'
                       '1 - добавить товар\n'
                       '2 - показать товары\n'
                       '3 - показать аналитику\n'
                       '4 - выйти\n'
                       'Введите число: ')
else:
    print('Выход из программы')
