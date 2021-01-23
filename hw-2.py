len_my_list = int(input('Напишите сколько элементов списка вы планируете добавить: '))

my_list = []

for i in range(len_my_list):
    my_list.append(input(f'Введите элемент списка №{i}: '))

shift_i = 0

for i in range(len_my_list // 2):
    i += shift_i
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    shift_i += 1

print(my_list)
