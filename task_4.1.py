def my_func(x, y):
    while y > 0:
        y = y*(-1)
    return x ** y


print(f'Возведение в степень v.1 : '
      f'{my_func(int(input("Число Х: ")), int(input("Показатель степени Y: ")))}')
