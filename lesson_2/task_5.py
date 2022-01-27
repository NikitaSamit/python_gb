user_data = [1, 3, 5, 7, 9]
print(f'Структура "Рейтинг" - {user_data}')
digit = int(input("Введите любое число (кроме 1994): "))
while digit != 1994:
    for a in range(len(user_data)):
        if user_data[a] == digit:
            user_data.insert(a + 1, digit)
            break
        elif user_data[0] < digit:
            user_data.insert(0, digit)
        elif user_data[-1] > digit:
            user_data.append(digit)
        elif user_data[a] > digit and user_data[a + 1] < digit:
            user_data.insert(a + 1, digit)
    print(f"Обновленный рейтинг: - {user_data}")
    digit = int(input("Введите еще одно число "))