import math
a = int(input('Enter a coefficient: \n'))
b = int(input('Enter b coefficient: \n'))
c = int(input('Enter c coefficient: \n'))
D = math.pow(b, 2) - 4 * a * c
if D < 0:
    print('No solutions')
elif D == 0:
    x = (b * (-1)) / 2 * a
    print('Solution is : ' + str(x))
elif D > 0:
    x1 = (b * (-1) - math.sqrt(D)) / 2 * a
    x2 = (b * (-1) + math.sqrt(D)) / 2 * a
    print('Solutions are: ' + str(x1) + ' and ' + str(x2))

