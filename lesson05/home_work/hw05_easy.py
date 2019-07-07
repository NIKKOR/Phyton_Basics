import os

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def mkdir_1_9():
    for i in range(1, 10):
        dir_name = 'dir_' + str(i)
        dir_path = os.path.join(os.getcwd(), dir_name)
        os.mkdir(dir_path)
def rmdir_1_9():
    for i in range(1, 10):
        dir_name = 'dir_' + str(i)
        dir_path = os.path.join(os.getcwd(), dir_name)
        os.rmdir(dir_path)
print(os.getcwd())
mkdir_1_9()
rmdir_1_9()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
