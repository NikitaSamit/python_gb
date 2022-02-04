from itertools import cycle

number = int(input("Введите стартовое целое число: "))
num_stop = number + 6

my_list = [i for i in range(num_stop)]
count = 0
for b in cycle(my_list):
    if count < num_stop + 10:
        print(b)
        count += 1
    else:
        break
