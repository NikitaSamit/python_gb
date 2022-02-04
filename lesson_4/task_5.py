from functools import reduce

my_list = [i for i in range(100, 1001, 2)]
print("Перечень четных чисел от 100 до 1000:\n", my_list)
print("Произведение всех четных числе от 100 до 1000:\n", reduce(lambda x,y: x*y, my_list))