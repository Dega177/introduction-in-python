from functools import reduce


def fact(numeral):
    for num in range(1, numeral + 1):
        yield reduce(lambda x, y: x * y, [i for i in range(1, num + 1)] if num != 0 else [1])


for el in fact(5):
    print(el)
