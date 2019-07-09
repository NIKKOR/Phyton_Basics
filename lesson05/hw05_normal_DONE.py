import os
import item_path
import content_dir


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def goto_dir():
    dir_name=input('Введите имя папки для перехода: ')
    try:
        os.chdir(item_path.do(dir_name))
        print('Папка {} стала текущей директорией'.format(dir_name))
    except Exception:
        'При смене директории возникла ошибка. Попробуйте ещё раз'


def content_all():
    dir_path_2=os.listdir(os.getcwd())
    print('{0:.^100}'.format('Содержимое текущей директории:') +
          '\n{0}{1:>57}'.format('Имя:', 'Путь:'))
    for i in dir_path_2:
        extra_path='({})'.format(item_path.do(i))
        print(i + '{0:>100}'.format(extra_path))


def del_dir():
    dir_name=input('Введите имя папки для удаления: ')
    try:
        os.rmdir(item_path.do(dir_name))
        print('Папка {} успешно удалена'.format(dir_name))
    except Exception:
        'При удалении папки возникла ошибка. Попробуйте ещё раз'


def mk_new_dir():
    dir_name=input('Введите имя новой папки: ')
    try:
        os.mkdir(item_path.do(dir_name))
        print('Папка {} успешно создана'.format(dir_name))
    except Exception:
        'При создании папки возникла ошибка. Попробуйте ещё раз'


def interface():
    print('\n\n\n{0:.^100}'.format('Файловый менеджер'))
    print('{0}{1:>60}'.format('1. Перейти в папку', 'Текущая директория: '))
    print('{0}{1:>60}'.format('2. Просмотреть содержимое текущей папки', os.getcwd()))
    print(
        '''3. Удалить папку
4. Создать папку'''
    )
    print('5. Выйти\n{0:.^100}'.format(''))
    try:
        print('Введите команду: ')
        command=input()
    except Exception:
        'Команда некорректна'
    if command == '1':
        goto_dir()
    elif command == '2':
        content_all()
    elif command == '3':
        del_dir()
    elif command == '4':
        mk_new_dir()
    elif command == '5':
        return "exit"
    else:
        print('Команда некорректна')


while True:
    if interface() == 'exit':
        break
    interface()
