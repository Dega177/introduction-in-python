def print_person_info(name, surname, year_of_birth, city, email, phone):
    print(f'Имя: {name}. Фамилия: {surname}. Год рождения: {year_of_birth}. '
          f'Город проживания: {city}. Почта: {email}. Телефон: {phone}')


person_info = {
    'name': 'Дмитрий',
    'surname': 'Филипов',
    'year_of_birth': '1988',
    'city': 'Москва',
    'email': 'd.filipov@gmail.com', 'phone': '+7 495-456-4547'}

print_person_info(
    name=person_info['name'],
    surname=person_info['surname'],
    year_of_birth=person_info['year_of_birth'],
    city=person_info['city'],
    email=person_info['email'],
    phone=person_info['phone'])
