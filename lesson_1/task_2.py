user_number = int(input("Введите количество секунд: "))
hh = (int(user_number / 3600))
mm = (int((user_number % 3600) / 60))
ss = (int((user_number % 3600) % 60))
result = f'Вы указали {user_number} секунд, это составляет {hh} ч. {mm} мин. {ss} сек. {hh:02}:{mm:02}:{ss:02}'
print(result)