import datetime


class Date:

    def __init__(self, date):
        self.day, self.month, self.year = date.split('-')

    @classmethod
    def date_to_int(cls, obj):
        obj.day, obj.month, obj.year = map(int, [obj.day, obj.month, obj.year])
        cls.validation(obj)

    @staticmethod
    def validation(obj):

        if obj.year < 2010:
            obj.year = 2010
            print(f'Год должен находится в рамках 2010-2021. Устанавливаем 2010')
        elif obj.year > 2021:
            obj.year = 2021
            print(f'Год должен находится в рамках 2010-2021. Устанавливаем 2021')

        if obj.month < 1:
            obj.month = 1
            print(f'Месяц должен находится в рамках 1-12. Устанавливаем 1')
        elif obj.month > 12:
            obj.month = 12
            print(f'Месяц должен находится в рамках 1-12. Устанавливаем 12')

        if obj.day < 1:
            obj.day = 1
            print('День не может быть меньше 1. Устанавливаем 1')
        else:
            next_month = datetime.date(obj.year, obj.month, 1) + datetime.timedelta(days=35)
            last_day = next_month.replace(day=1) - datetime.timedelta(days=1)
            if last_day.day < obj.day:
                print(f'В месяце {obj.month} года {obj.year} меньше {obj.day} дней. Устанавливаем {last_day.day}')
                obj.day = last_day.day


user_date = input('Введите дату в формате дд-мм-гггг: ')
if user_date.isalpha() or '-' not in user_date:
    print('Вы ввели дату в неверном формате')
else:
    date = Date(user_date)
    Date.date_to_int(date)
    print(date.day)
    print(date.month)
    print(date.year)
