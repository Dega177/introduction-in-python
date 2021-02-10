class Cell:

    def __init__(self, cell_number):
        self.cell_number = cell_number

    def __add__(self, other):
        return Cell(self.cell_number + other.cell_number)

    def __sub__(self, other):
        if self.cell_number > other.cell_number:
            return Cell(self.cell_number - other.cell_number)
        else:
            raise ValueError('Количество ячеек у первого объекта меньше, чем у второго')

    def __mul__(self, other):
        return Cell(self.cell_number * other.cell_number)

    def __truediv__(self, other):
        result = self.cell_number // other.cell_number
        if result != 0:
            return Cell(result)
        else:
            raise ValueError('Количество ячеек первой клетки слишком мало для деления')

    def make_order(self, row_length):
        for _ in range(self.cell_number // row_length):
            print('*' * row_length)
        print('*' * (self.cell_number % row_length))


cell_1 = Cell(15)
cell_2 = Cell(10)

print((cell_1 + cell_2).cell_number)
print((cell_1 - cell_2).cell_number)
print((cell_1 * cell_2).cell_number)
print((cell_1 / cell_2).cell_number)

print()
cell_1.make_order(4)
