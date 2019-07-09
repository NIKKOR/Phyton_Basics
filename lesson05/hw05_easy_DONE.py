import os, sys, content_dir, shutil, item_path


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

try:
    mkdir_name_x_to_y('dir_', 1, 9)
    content_dir.do()
finally:
    rmdir_name_x_to_y('dir_', 1, 9)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

item_name=str(os.path.basename(sys.argv[0]))[:-3]
shutil.copyfile(item_path.do(item_name + '.py'), item_path.do(item_name + '_copy.py'))
