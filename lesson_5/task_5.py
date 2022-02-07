def summary():
    try:
        with open('lesson_5_task_5.txt', 'w+') as file_obj:
            line = input('Введите любые целые числа через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


summary()
