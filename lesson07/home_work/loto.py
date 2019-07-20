#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random

ran_nums_base = sorted(random.sample(range(1, 90), 5)) \
                + sorted(random.sample(range(1, 90), 5)) \
                + sorted(random.sample(range(1, 90), 5))


def get_ran_nums_base():
    return sorted(random.sample(range(1, 90), 5)) \
           + sorted(random.sample(range(1, 90), 5)) \
           + sorted(random.sample(range(1, 90), 5))


def get_ran_index_row(rows: int = 1):
    random_index_row = []
    for _ in range(0, rows):
        random_index_row.append(sorted(random.sample(range(0, 9), 5)))
    return random_index_row


class Row:
    def __init__(self, order: int = 1, property: str = 'Human'):
        self.order = order
        self.row = ["_" for _ in range(0, 9)]
        self.ran_nums_base_index = 5 * (order - 1)
        self.ran_index_row_temp = get_ran_index_row(order)[order - 1]
        ran_nums_base_tmp = get_ran_nums_base()
        for index_range in range(0, 9):
            if index_range in self.ran_index_row_temp:
                self.row[index_range] = ran_nums_base_tmp[self.ran_nums_base_index]
                self.ran_nums_base_index += 1
        self.row_str = ''
        for el in self.row:
            self.row_str += str(el) + ' '

    def __str__(self):
        return f'{str(self.row_str)}'


class Card:
    def __init__(self, property: str = 'Human'):
        self.first = str(Row(1))
        self.second = str(Row(2))
        self.third = str(Row(3))
        rows_data = f'{Row(1)}\n{Row(2)}\n{Row(3)}'
        print('{0:.^25}'.format('Ваша карточка' if property == 'Human'
                                else 'Карточка компьютера'))
        print(rows_data)
        print('{0:.^25}\n'.format(''))

a = Card('Human')
b = Card('Computer')

digits_base = [i for i in range(1, 91)]

queue = []
