class Warehouse:

    def __init__(self, code, capacity):
        self.code = code
        self.capacity = capacity
        self.workload = 0
        self.items = {}

    def __str__(self):
        return f'Код склада {self.code}. Свободно {self.current_capacity} мест из {self.capacity}'

    @property
    def current_capacity(self):
        return self.capacity - self.workload

    def take_items(self, product, amount):
        if self.workload + amount <= self.capacity:
            self.items[product.code] = {'item': product.pack, 'amount': amount}
            self.workload += amount
            print('Товары добавлены на склад')
        else:
            print(f'На склад можно разместить не больше {self.current_capacity} товаров')

    def get_items_info(self):
        result = ''
        for key in self.items:
            result += f'Code: {key}: {self.items[key]}\n'
        return result

    def send_to_the_unit(self, unit_code, product_code, amount):
        if amount <= self.items[product_code]['amount']:
            Unit.units[unit_code]['items'][product_code] = dict(self.items[product_code]['item'])
            Unit.units[unit_code]['items'][product_code]['amount'] = amount
            self.items[product_code]['amount'] -= amount
            self.workload -= amount
            if self.items[product_code]['amount'] == 0:
                del(self.items[product_code])
        else:
            print('На складе недостаточно товаров')


class Unit:

    units = {}

    def __init__(self, code, capacity):
        Unit.units = {code: {'capacity': capacity, 'workload': 0, 'items': {}}}

    @classmethod
    def current_capacity(cls, units_code):
        return cls.units[units_code]['capacity'] - cls.units[units_code]['workload']

    @classmethod
    def units_info(cls):
        result = ''
        for key in cls.units:
            result += f'Code: {key}. Info: {cls.units[key]}\n'
        return result

    @classmethod
    def to_sell(cls, unit_code, product_code, amount):
        if amount <= Unit.units[unit_code]['items'][product_code]['amount']:
            cls.units[unit_code]['items'][product_code]['amount'] -= amount
            cls.units[unit_code]['workload'] -= amount
            if cls.units[unit_code]['items'][product_code]['amount'] == 0:
                del(cls.units[unit_code]['items'][product_code])
        else:
            print('В подразделении недостаточно товаров')


class OfficeEquipment:

    def __init__(self, code, brand, model):
        self.code = code
        self.brand = brand
        self.model = model


class Printer(OfficeEquipment):

    def __init__(self, code, brand, model, print_technology, paper_format, number_of_colors, equipment_type='Printer'):
        super().__init__(code, brand, model)
        self.equipment_type = equipment_type
        self.print_technology = print_technology
        self.paper_format = paper_format
        self.number_of_colors = number_of_colors

    @property
    def pack(self):
        return {
            'equipment_type': self.equipment_type,
            'brand': self.brand,
            'model': self.model,
            'print_technology': self.print_technology,
            'paper_format': self.paper_format,
            'number_of_colors': self.number_of_colors
        }


class Scanner(OfficeEquipment):

    def __init__(self, code, brand, model, scan_technology, paper_format, resolutions, equipment_type='Scanner'):
        super().__init__(code, brand, model)
        self.equipment_type = equipment_type
        self.scan_technology = scan_technology
        self.paper_format = paper_format
        self.resolutions = resolutions

    @property
    def pack(self):
        return {
            'equipment_type': self.equipment_type,
            'brand': self.brand,
            'model': self.model,
            'scan_technology': self.scan_technology,
            'paper_format': self.paper_format,
            'resolutions': self.resolutions
        }


class Copier(OfficeEquipment):

    def __init__(self, code, brand, model, copy_speed, copy_cost, copy_resource, equipment_type='Copier'):
        super().__init__(code, brand, model)
        self.equipment_type = equipment_type
        self.copy_speed = copy_speed
        self.copy_cost = copy_cost
        self.copy_resource = copy_resource

    @property
    def pack(self):
        return {
            'equipment_type': self.equipment_type,
            'brand': self.brand,
            'model': self.model,
            'copy_speed': self.copy_speed,
            'copy_cost': self.copy_cost,
            'copy_resource': self.copy_resource
        }
