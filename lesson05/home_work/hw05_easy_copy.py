import os
from shutil import copyfile
import sys

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def mkdir_name_x_to_y(dir_name_def, x, y):
    for i in range(x, y + 1):
        dir_name=dir_name_def + str(i)
        dir_path=os.path.join(os.getcwd(), dir_name)
        os.mkdir(dir_path)


def rmdir_name_x_to_y(dir_name_def, x, y):
    for i in range(x, y + 1):
        dir_name=dir_name_def + str(i)
        dir_path=os.path.join(os.getcwd(), dir_name)
        os.rmdir(dir_path)


mkdir_name_x_to_y('dir_', 1, 9)
rmdir_name_x_to_y('dir_', 1, 9)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import task1

def item_path(item):
    return os.path.join(os.getcwd(), item)


try:
    task1.mkdir_name_x_to_y('dir_', 1, 9)

    dir_path_2 = os.listdir(os.getcwd())
    print('\n{0:.^50}'.format('Папки текущей директории:') +
          '\n{0}{1:.>38}'.format('Имя папки:', 'Путь к папке:'))
    for i in dir_path_2:
        extra_path = '({})'.format(item_path(i))
        if os.path.isdir(item_path(i)):
            print(i, '{:.>100}'.format(extra_path))
finally:
    task1.rmdir_name_x_to_y('dir_', 1, 9)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import task2

item_name = str(os.path.basename(sys.argv[0]))[:-3]
copyfile(task2.item_path(item_name + '.py'), task2.item_path(item_name + '_copy.py'))
