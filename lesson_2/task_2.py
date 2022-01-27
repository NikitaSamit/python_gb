amount_elements = int(input("Введите количесвто элементов: "))
user_data = []
a = 0
b = 0
while a < amount_elements:
    user_data.append(input("Введите элемент:"))
    a += 1
for element in range(int(len(user_data) / 2)):
    user_data[b], user_data[b + 1] = user_data[b + 1], user_data[b]
    b += 2
print(user_data)
