user_profit = float(input("Введите приблыль: "))
user_costs = float(input("Введите издержки: "))
if user_profit > user_costs:
    print(f'Фирма работет в плюс с рентабельностью {user_profit / user_costs} ')
    employees = int(input("Введите количество сотрудников:" ))
    print(f'Прибыль фирмы в расчёте на одного сотрудника составила: {user_profit / employees}')
elif user_profit==user_costs:
    print("Фирма не зарабатывает и не теряет деньги, работает в ноль")
else:
    print("Фирма работает в минус")
