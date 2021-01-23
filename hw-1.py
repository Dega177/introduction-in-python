my_list = [1, 1.5, [2, 4], (2, 4), {2: 3, 4: 5}, 1+2j, None, 'some text']

for i, el in enumerate(my_list, 1):
    print(i, type(el))
