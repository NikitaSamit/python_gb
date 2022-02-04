from itertools import cycle, count

number = int(input("Введите стартовое целое число: "))
num_stop = 11

for i in count(number):
    if i < num_stop:
        print(i)
    else:
        break
del i
