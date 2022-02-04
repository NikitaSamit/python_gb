final_list = []
my_list = [int(i) for i in input("Введите чисела через пробел: ").split()]
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        (final_list.append(my_list[i]))
print("Входные данные: ", my_list)
print("Элементы, которые больше предшественника: ", final_list)
