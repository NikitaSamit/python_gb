user_data = input("Введите любые данные через разделив пробелом: ")
one_word = []
number = 1
for a in range(user_data.count(' ') + 1):
    one_word = user_data.split()
    if len(str(one_word)) <= 10:
        print(f" {number} {one_word [a]}")
        number += 1
    else:
        print(f" {number} {one_word [a] [0:10]}")
        number += 1