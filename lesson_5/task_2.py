def count_info():
    try:
        with open('lesson_5_task_2.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            for i in range(len(my_list)):
                new_l = my_list[i].split()
                print(f'Количество строк в моем файле {len(my_list)}. Количество слов в {i + 1}-ой строке {len(new_l)} слов(а)')
    except FileNotFoundError:
        return 'Файл с указанным именем не найден.'


count_info()
