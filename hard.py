a = float('inf')
pow = a == a**2
double = a == a*2
big = a > 999999
print('a = float("inf") ' + '\n' +
      'a == a**2: ' + str(pow) + "\n" +
      'a == a*2: ' + str(double) + "\n" +
      'a > 999999: ' + str(big) + "\n" +
      'That is ' + str(a) +  ' (infinity)')
