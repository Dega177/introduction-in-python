with open('text_1_2.txt', 'w+', encoding='utf-8') as file:
    data = 'str'
    while data:
        data = input('Введите данные для записи: ')
        if data:
            file.write(data + '\n')

    file.seek(0)
    line_count = 0
    for line in file:
        line_count += 1
        print(f'В строке {line_count} содержится {len(line)} символ(а/ов)')
    else:
        print(f'Всего строк {line_count}')
