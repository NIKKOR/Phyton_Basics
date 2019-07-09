import os
import task1


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
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
