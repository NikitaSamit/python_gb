user_number = int(input("Введите любое целое число:"))
m = 0
while user_number > 0:
    mx = user_number % 10
    if mx >= m: m=mx
    user_number//=10
print(m)
