first_day_km = int(input("Введите количество километров преодаленное в первый день: "))
mx_km = int(input("Введите максимальное количество километров: "))
result_km = first_day_km
final_day = 1
while first_day_km < mx_km:
    first_day_km = first_day_km + first_day_km * 0.1
    final_day += 1
    result_km = result_km + first_day_km
print(f'Спортсмен пробежит {mx_km} километров за {final_day}')


