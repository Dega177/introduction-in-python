class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    num_1 = float(input('Введите делимое: '))
    num_2 = float(input('Введите делитель: '))

    if num_2 == 0:
        raise MyZeroDivisionError('Делить на 0 нельзя')
    else:
        print(num_1 / num_2)
except MyZeroDivisionError as err:
    print(err)
