import os, item_path

def do():
    dir_path_2=os.listdir(os.getcwd())
    print('\n{0:.^50}'.format('Папки текущей директории:') +
          '\n{0}{1:.>38}'.format('Имя папки:', 'Путь к папке:'))
    for i in dir_path_2:
        extra_path='({})'.format(item_path.do(i))
        if os.path.isdir(item_path.do(i)):
            print(i, '{:.>100}'.format(extra_path))
