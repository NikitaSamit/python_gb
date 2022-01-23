user_input = input("Введите число: ")
n = int(user_input)
nn = int(user_input + user_input)
nnn = int(user_input + user_input + user_input)
answer = n + nn + nnn
result = f'Решение задачи: {n} + {nn} + {nnn} = {answer}'
print(result)
