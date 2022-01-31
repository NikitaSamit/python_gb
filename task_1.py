def div(*args):
    try:
        arg1 = int(input("Введите числитель "))
        arg2 = int(input("Введите знаменатель "))
        res = arg1 / arg2
    except ValueError:
        return 'Это уже будет умножение'
    except ZeroDivisionError:
        return "На ноль делить нельзя"

    return res


print(f'Ответ  {div()}')
