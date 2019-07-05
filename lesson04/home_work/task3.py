import re
import random

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

file = open('file.txt', 'w+')
file_text_list = []
file_text_str = ''
for _ in range(0, 2500):
    file_text_list.append(random.randint(0,9))
for i in file_text_list:
    file_text_str += str(i)
file.write(file_text_str)
count = 1
count_tmp = 0
count_list = []
count_list_tmp = []
for i, el in enumerate(file_text_str):
    if i != 0 and file_text_str[i] == file_text_str[i-1]:
        count += 1
        count_list.append(el)
    else:
        if count > count_tmp:
            count_tmp = count
            count_list_tmp = count_list
        count = 1
        count_list = []
count_list_tmp = count_list_tmp[0]*len(count_list_tmp)
print(count_list_tmp)
