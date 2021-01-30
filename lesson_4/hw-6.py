from itertools import count, cycle, islice

[print(num) for num in islice(count(10), 20)]

[print(el) for el in islice(cycle(['A', 'B', 'C', 'D']), 20)]
