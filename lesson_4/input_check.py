def is_number(num, check_type):
    if check_type == 'int':
        try:
            list(map(int, num))
            return True
        except ValueError:
            return False
    elif check_type == 'float':
        try:
            list(map(float, num))
            return True
        except ValueError:
            return False
