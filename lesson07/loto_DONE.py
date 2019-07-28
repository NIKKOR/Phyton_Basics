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

num_offered_base = [num for num in range(1, 91)]

rows = 3
columns = 9

class Card:
    def __init__(self, property):
        self.data = [[' ' for _ in range(columns)] for _ in range(rows)]
        self.property = property
        self.first_el_human = False
        self.first_el_computer = False

        row_nums_base = [_ for _ in range(1, 91)]
        # self.row_nums = [sorted(random.sample(row_nums_base, 5)) for _ in range(3)]
        self.row_nums = [[' ' for _ in range(5)] for _ in range(rows)]
        for i in range(rows):
            for y in range(5):
                self.row_nums[i][y] = random.choice(row_nums_base)
                if y == 0 and i == 0 and property == 'Human':
                    self.first_el_human = self.row_nums[i][y]
                elif y == 0 and i == 0 and property == 'Computer':
                    self.first_el_computer = self.row_nums[i][y]
                row_nums_base.remove(self.row_nums[i][y])
            self.row_nums[i] = sorted(self.row_nums[i])
        row_indexes = [sorted(random.sample(range(columns), 5)) for _ in range(3)]
        for row in range(rows):
            for i, el in enumerate(self.data[row]):
                if i in row_indexes[row]:
                    self.data[row][i] = self.row_nums[row][0]
                    self.row_nums[row].remove(self.row_nums[row][0])

    def data_print(self, data_row):
        self.data_row = data_row
        self.data_row_str = ''
        for el in self.data_row:
            self.data_row_str += str(el) + ' '
        return self.data_row_str

    def print(self, property):
        print('{0:.^25}\n{1:^25}\n'
              '{2:^25}\n{3:^25}\n'
              '{4:.^25}'.format(
            'Ваша карточка' if property == 'Human' else 'Карточка компьютера',
            f'{self.data_print(self.data[0])}',
            f'{self.data_print(self.data[1])}',
            f'{self.data_print(self.data[2])}', ''))

def print_num_offered(card, base_def):
    base = base_def
    global first_el_check_human
    global first_el_check_computer
    global nums_count
    ran_num = random.choice(base)
    print(f'\nНовый бочонок: {ran_num} (осталось {len(base)})')
    base.remove(ran_num)
    nums_count -= 1
    return [base, ran_num]

def endgame(player):
    return True, f'{player} проиграл. Победитель - {"Человек" if player == "Компьютер" else "Компьютер"}'

def endgame_full(player):
    return endgame(player)[0], endgame(player)[1]

human_card = Card('Human')
computer_card = Card('Computer')
quit_check = False
human_count = 0
computer_count = 0
nums_count = 90
queue = 0
debug_mode = 0
first_el_check_human = 0
first_el_check_computer = 0
while quit_check == 0:
    if queue == 0:
        num_offered_full = print_num_offered(human_card, num_offered_base)
        num_offered_base = num_offered_full[0]
        num_offered = num_offered_full[1]
        human_card.print('Human')
        computer_card.print('Computer')

        if debug_mode == 1:
            choice = 'n'
            for row in range(rows):
                if num_offered in human_card.data[row]:
                    choice = 'y'
            print(f'Выбор человека: {choice}')
        else:
            choice = input('Зачеркнуть цифру (y/n)\n')
        if choice == 'y':
            win_check = False
            for row in range(rows):
                if num_offered in human_card.data[row]:
                    human_card.data[row][human_card.data[row].index(num_offered)] ='X'
                    human_count += 1
                    win_check = True
            if  win_check == False:
                print(endgame_full('Человек')[1])
                quit_check = endgame_full('Человек')[0]
        else:
            for row in range(rows):
                if num_offered in human_card.data[row]:
                    print(endgame_full('Человек')[1])
                    quit_check = endgame_full('Человек')[0]

        queue = 1
        continue

    else:
        # Очередь компьюетра
        num_offered_full = print_num_offered(computer_card, num_offered_base)
        num_offered_base = num_offered_full[0]
        num_offered = num_offered_full[1]
        computer_card.print('Computer')
        human_card.print('Human')
        print('Зачеркнуть цифру (y/n)\n')
        choice = 'n'
        for row in range(rows):
            if num_offered in computer_card.data[row]:
                choice = 'y'

        print(f'Выбор компьютера: {choice}')
        if choice == 'y':
            win_check = False
            for row in range(rows):
                if num_offered in computer_card.data[row]:
                    computer_card.data[row][computer_card.data[row].index(num_offered)] = \
                    'X'
                    computer_count += 1
                    win_check = True
            if win_check == False:
                print(endgame_full('Компьютер')[1])
                quit_check = endgame_full('Компьютер')[0]
        else:
            for row in range(rows):
                if num_offered in computer_card.data[row]:
                    print(endgame_full('Компьютер')[1])
                    quit_check = endgame_full('Компьютер')[0]

    queue = 0

    if computer_count == 15:
        endgame_full('Человек')
        quit_check = endgame_full('Человек')[0]
    elif human_count == 15:
        endgame_full('Компьютер')
        quit_check = endgame_full('Компьютер')[0]

    if nums_count == 0 and human_count > computer_count:
        print(f'Ходы закончились, побеждает игрок с наибольшим количеством зачеркнутых чисел\n'
              f'{endgame_full("Компьютер")[1] if human_count > computer_count else endgame_full("Компьютер")[1]}')
        quit_check = endgame_full('Компьютер')[0] if human_count > computer_count else endgame_full("Компьютер")[1]
