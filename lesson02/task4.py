def input_infinity_list(list_def: list, keyword: str):
    while True:
        list_def.append(input('Вводите элементы списка. Когда закончите, введите в поле ввода "EXIT"\n'))
        if list_def[-1] == keyword:  # проверка на ключевое слово EXIT
            list_def.pop()  # убираем EXIT из списка
            print('Ваш исходный список: ', list_def)  # выводим данный список
            break  # выходим из бесконечного цикла (приходится так делать, ведь do-while в phyton нет(((
        elif not list_def[-1].isalpha():  # преобразуем строку в число для дальнейших математических операций
            # (введённые числа преобразуются в строку с помощью input)
            if float(list_def[-1]) % 1 == 0:
                list_def[-1] = int(float(list_def[-1]))
            else:
                list_def.pop()
                print('Можно вводить только целые числа')
        else:
            list_def.pop()
            print('Можно вводить только целые числа')

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

list_4 = []
input_infinity_list(list_4, 'EXIT')

list_4_a = sorted(set(list_4))
list_4_a_text = 'а) Ваш список с неповторяющимися элементми исходного списка: ' + str(list_4_a)

list_4_b = []
for i in range(0, len(list_4)):
    if list_4[i] not in list_4_b:
        list_4_b.append(list_4[i])
    else:
        list_4_b.remove(list_4_b[i])
list_4_b_text = 'б) Ваш список с элементми исходного списка, которые не имеют повторений: ' + str(list_4_b)


print(list_4_a_text + '\n' + list_4_b_text)





