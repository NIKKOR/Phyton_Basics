__author__ = 'Коробкин Никита Дмитриевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

print('---First Problem---')
number = str(input('Enter a number \n'))
symMax = 0
for sym in number:
    if int(sym) > symMax:
        symMax = int(sym)
print(symMax, '\n')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print('---Second Problem---')
a = int(input('Enter first number\n'))
b = int(input('Enter second number\n'))
a = a, b,
b = a[0]
a = a[1]

print('Now: a = ' + str(a) + ' and b = ' + str(b), '\n')
# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print('---Third Problem---')
import math
a = float(input('Enter a coefficient: \n'))
b = float(input('Enter b coefficient: \n'))
c = float(input('Enter c coefficient: \n'))
D = math.pow(b, 2) - 4 * a * c
if D < 0:
    print('No solutions')
elif D == 0:
    x = (b * (-1)) / 2 * a
    print('Solution is : ' + str(x))
elif D > 0:
    x1 = (b * (-1) - math.sqrt(D)) / 2 * a
    x2 = (b * (-1) + math.sqrt(D)) / 2 * a
    print('Solutions are: ' + str(x1) + ' and ' + str(x2), '\n')
