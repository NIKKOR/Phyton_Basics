import os


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

#  добавь удаление перед запуском
