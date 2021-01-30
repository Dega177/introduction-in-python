from functools import reduce

num_list = [num for num in range(10, 1001) if num % 2 == 0]

print(reduce(lambda x, y: x * y, num_list))
