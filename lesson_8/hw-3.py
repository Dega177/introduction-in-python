class NotANumber(Exception):
    def __init__(self, txt):
        self.txt = txt


result = []
user_input = ''

while user_input != 'Q':

    try:
        user_input = input('Введите число или "Q" для выхода: ')

        if user_input.isalpha() and 'Q' not in user_input.upper():
            raise NotANumber('Можно вводить только числа')
        elif 'Q' in user_input.upper():
            user_input = 'Q'
        else:
            result.append(float(user_input))
    except NotANumber as err:
        print(err)

print(result)
