def get_sum_max_argv(a, b, c):
    numbers = [a, b, c]
    numbers.remove(min([a, b, c]))
    return sum(numbers)


print(get_sum_max_argv(12, 15, 17))
