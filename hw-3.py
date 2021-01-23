months = [
    'Январь', 'Февраль', 'Март',
    'Апрель', 'Май', 'Июнь',
    'Июль', 'Август', 'Сентябрь',
    'Октябрь', 'Ноябрь', 'Декабрь']

seasons = {
    'Январь': 'Зима',
    'Февраль': 'Зима',
    'Март': 'Весна',
    'Апрель': 'Весна',
    'Май': 'Весна',
    'Июнь': 'Лето',
    'Июль': 'Лето',
    'Август': 'Лето',
    'Сентябрь': 'Осень',
    'Октябрь': 'Осень',
    'Ноябрь': 'Осень',
    'Декабрь': 'Зима'}

user_month = int(input('Введите номер месяца от 1 до 12: '))

print(f'Вы выбрали месяц - {months[user_month - 1]}\n'
      f'Это - {seasons[months[user_month - 1]]}')
