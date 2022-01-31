def user_data(name, lastname, year, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year} Город проживания: {city} Email: {email} Телефон: {phone}')


user_data(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)