import os


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def mkdir_x_to_y(x, y):
    for i in range(x, y + 1):
        dir_name='dir_' + str(i)
        dir_path=os.path.join(os.getcwd(), dir_name)
        os.mkdir(dir_path)


def rmdir_x_to_y(x, y):
    for i in range(x, y + 1):
        dir_name='dir_' + str(i)
        dir_path=os.path.join(os.getcwd(), dir_name)
        os.rmdir(dir_path)


print(os.getcwd())
mkdir_x_to_y(1, 9)
rmdir_x_to_y(1, 9)

#  добавь удаление перед запуском
