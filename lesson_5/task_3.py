def wor_info():
    try:
        with open('lesson_5_task_3.txt', 'r', encoding="utf-8") as file:
            sal = []
            poor = []
            my_list = file.read().split('\n')
            for i in my_list:
                i = i.split()
                if int(i[1]) < 20000:
                    poor.append(i[0])
                    sal.append(i[1])
                print(f'Оклад до 20000 {poor}. Средний оклад: {sum(map(int, sal)) / len(sal)}')
    except FileNotFoundError:
        return 'Файл с указанным именем не найден.'


wor_info()
