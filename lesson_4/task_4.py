my_list = [9, 9, 7, 7, 4, 3, 2, 2, 22, 1]
print("Исходные элементы списка:\n", my_list)
final_list = [i for i in my_list if my_list.count(i) == 1]
print("Элементы списка, не имеющие повторений:\n", final_list)
