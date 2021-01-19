user_number = int(input('Введите целое положительное число: '))

max_number = 0
while user_number != 0:
    number = user_number % 10
    if max_number < number:
        max_number = number
    user_number //= 10

print(max_number)
