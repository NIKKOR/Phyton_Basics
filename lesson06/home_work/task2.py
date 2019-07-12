import math


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trap:
    def __init__(self,
                 x1, y1,
                 x2, y2,
                 x3, y3,
                 x4, y4):
        self.a=[x1, y1]
        self.b=[x2, y2]
        self.c=[x3, y3]
        self.d=[x4, y4]
        self.ab=math.sqrt((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2)
        self.bc=math.sqrt((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2)
        self.cd=math.sqrt((self.c[0] - self.d[0]) ** 2 + (self.c[1] - self.d[1]) ** 2)
        self.ad=math.sqrt((self.a[0] - self.d[0]) ** 2 + (self.a[1] - self.d[1]) ** 2)

    def p(self):
        return self.ab + self.bc + self.cd + self.ad

    def isosceles(self):
        if self.ab == self.cd or self.bc == self.ad:
            print('Трапеция равнобедренная')
        else:
            print('Трапеция не равнобедренная')

    def parallels(self):
        if self.ab == self.cd:
            return [self.bc, self.ad]
        elif self.bc == self.ad:
            return [self.ab, self.cd]
        else:
            print('Трапеция не равнобедренная')

    def h(self):
        if self.parallels() == [self.bc, self.ad]:
            if self.b[1] > self.a[1]:
                return self.b[1] - self.a[1]
            else:
                return self.a[1] - self.b[1]
        elif self.parallels() == [self.ab, self.cd]:
            if self.b[1] > self.d[1]:
                return self.b[1] - self.d[1]
            else:
                return self.d[1] - self.b[1]

    def s(self):
        return 0.5 * (self.parallels()[0] + self.parallels()[1]) * self.h()


trap=Trap(0.5,1.5,1.5,4,2.5,4,3.5,1.5)
print(trap.s())
