distance = int(input('Введите дистанцию первого дня: '))
target_distance = int(input('Введите целевую дистанцию: '))

day_count = 1

if distance == target_distance:
    print(f'Спортсмен достигнет цели в {target_distance} км. на {day_count} день')

while distance < target_distance:
    distance *= 1.1
    if distance >= target_distance:
        print(f'Спортсмен достигнет цели в {target_distance} км. на {day_count + 1} день')
    day_count += 1
