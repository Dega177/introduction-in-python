def upper_first_letter(some_text):
    """Принимает строку, переводит первую букву каждого слова в верхний регистр."""
    return some_text.title()


def has_cyrillic(some_text):
    """Проверяет входят ли в строку символы кирилического алфавита

    some_text -- текстовая строка
    cyrillic_alphabet -- множество со всеми буквами кирилического алфавита

    Проверка выполняется путем пересечения множества алфавита со строкой.
    Если при пересечении получаем пустое множество,
    то в строке нет кирилических букв - функция вернет False
    Если получим не пустое множество - в строке есть символы кирилицы -
    функция вернет True

    """
    cyrillic_alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    return cyrillic_alphabet.intersection(some_text.lower()) != set()


words = input('Введите слова через пробел: ').split()

result = [upper_first_letter(word) for word in words if not has_cyrillic(word)]

print(' '.join(result))
