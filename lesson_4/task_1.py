def salary_calc():
    hh = float(input('Количество выработаных часов: '))
    peronehh = float(input('Ставка за 1 час работы: '))
    premium = float(input('Премя составила: '))
    salary = hh * peronehh
    return salary + premium


print(f'Размер заработной платы составил: {salary_calc()}')
