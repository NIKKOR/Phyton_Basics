from shutil import copyfile
import os, sys
from task2 import item_path
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
item_name = str(os.path.basename(sys.argv[0]))[:-3]
copyfile(item_path(item_name + '.py'), item_path(item_name + '_copy.py'))
