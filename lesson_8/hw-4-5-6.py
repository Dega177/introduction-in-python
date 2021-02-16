from classes import Warehouse, Unit, Printer, Scanner, Copier


def input_check(txt):
    while True:
        num = input(txt)
        try:
            num = int(num)
            if num > 0:
                return num
            else:
                raise ValueError
        except ValueError:
            print(f'Нужно ввести целое положительное число')


def check_unit_code():
    while True:
        result = input(f'Введите код подразделения, в которое нужно отправить товар:\n'
                       f'{Unit.units_info()}\n')
        if result not in Unit.units:
            print(f'Подразделение с кодом {result} не существует')
        else:
            return result


def check_product_code():
    while True:
        result = input(f'Введите код товара, который необходимо переместить в подразделение:\n'
                       f'{warehouse_1.get_items_info()}\n')
        if result not in warehouse_1.items:
            print(f'Товара с кодом {result} не существует')
        else:
            return result


user_input = 0

while user_input != 5:
    if user_input == 0:
        print('Необходимо создать первый склад')
        warehouse_code = input('Введите кодовое обозначение склада: ')
        warehouse_capacity = input_check('Введите количество мест на складе: ')
        warehouse_1 = Warehouse(warehouse_code, warehouse_capacity)
        print(f'Склад {warehouse_code} с количеством мест {warehouse_capacity} создан')

        print('Необходимо создать первое подразделение')
        unit_code = input('Введите кодовое обозначение подразделения: ')
        unit_capacity = input_check('Введите количество мест в подразделении: ')
        Unit(unit_code, unit_capacity)
        print(f'Подразделение {unit_code} с количеством мест {unit_capacity} создано')

    elif user_input == 1:
        product_type = int(input('Введите число, чтобы выбрать какой товар необходимо добавить:\n'
                                 '1 - добавить принтер\n'
                                 '2 - добавить сканнер\n'
                                 '3 - добавить копир\n'))
        if product_type == 1:
            printer = Printer(
                code=input('Введите кодовое обозначение принтера: '),
                brand=input('Введите бренд: '),
                model=input('Введите модель: '),
                print_technology=input('Введите способ печати: '),
                paper_format=input('Введите формат бумаги: '),
                number_of_colors=input('Введите количество цветов печати: '),
            )
            product_amount = input_check('Укажите сколько товаров нужно добавить на склад: ')
            warehouse_1.take_items(printer, product_amount)
        elif product_type == 2:
            scanner = Scanner(
                code=input('Введите кодовое обозначение сканнера: '),
                brand=input('Введите бренд: '),
                model=input('Введите модель: '),
                scan_technology=input('Введите технологию сканирования: '),
                paper_format=input('Введите формат бумаги: '),
                resolutions=input('Введите разрешение сканирования: '),
            )
            product_amount = input_check('Укажите сколько товаров нужно добавить на склад: ')
            warehouse_1.take_items(scanner, product_amount)
        elif product_type == 3:
            copier = Copier(
                code=input('Введите кодовое обозначение копира: '),
                brand=input('Введите бренд: '),
                model=input('Введите модель: '),
                copy_speed=input('Введите скорость сканирования: '),
                copy_cost=input('Введите стоимость копирования одного листа: '),
                copy_resource=input('Введите сколько листов можно копировать на одном картридже: '),
            )
            product_amount = input_check('Укажите сколько товаров нужно добавить на склад: ')
            warehouse_1.take_items(copier, product_amount)
    elif user_input == 2:
        if warehouse_1.items:
            unit_code = check_unit_code()
            product_code = check_product_code()
            product_amount = input_check('Введите количество товара, которое необходимо перевести: ')
            warehouse_1.send_to_the_unit(unit_code, product_code, product_amount)
        else:
            print('На складе нет товаров. Сначала добавьте товары')
    elif user_input == 3:
        unit_code = check_unit_code()
        product_code = check_product_code()
        product_amount = input_check('Введите количество товара, которое необходимо перевести: ')
        Unit.to_sell(unit_code, product_code, product_amount)
        print(f'{product_amount} товаров под кодом {product_code} продано из подразделения {unit_code}')
    elif user_input == 4:
        print(warehouse_1.get_items_info())

    user_input = int(input('Введите число, чтобы выбрать следующее действие:\n'
                           '1 - Добавить товары на склад\n'
                           '2 - Переместить товары со склада в подразделение\n'
                           '3 - Продать товары в подразделении\n'
                           '4 - Посмотреть товары на складе\n'
                           '5 - Завершить работу\n'))
else:
    print('Программа завершена')
