s_list = ['Зима', 'Весна', 'Лето', 'Осень']
s_dict = {1212: 'Зима', 345: 'Весна', 678: 'Лето', 91011: 'Осень'}
month = int(input("Назову время года по номеру месяца, укажите цифру от 1 до 12: "))
if month == 12 or month == 1 or month == 2:
    print(s_list[0])
    print(s_list.get(1212))
elif month == 3 or month == 4 or month == 5:
    print(s_list[1])
    print(s_dict.get(345))
elif month == 6 or month == 7 or month == 8:
    print(s_list[2])
    print(s_dict.get(678))
elif month == 9 or month == 10 or month == 11:
    print(s_list[3])
    print(s_dict.get(91011))
else:
    print("Серьезно? Всего 12 месяцев! Введите от 1 до 12 (включительно)")
