from random import randint

origin_list = [randint(0, 300) for _ in range(20)]

new_list_slice = [num for num in origin_list[1:] if num > origin_list[origin_list.index(num) - 1]]

new_list_range = [origin_list[i] for i in range(1, len(origin_list)) if origin_list[i] > origin_list[i - 1]]

new_list_enumerate = [v for i, v in enumerate(origin_list[1:], 1) if v > origin_list[i - 1]]

print(new_list_slice)
print(new_list_range)
print(new_list_enumerate)
