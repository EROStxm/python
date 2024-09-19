# DADO UN NUMERO SACAR LOS DIGITOS CENTRALES Y PONERLOS DE LOS EXTERNOS
import math
n = int(input("Intro n:"))
cd = int(math.log10(n))+1
if cd % 2 == 0:
    p = (cd//2)-1
else:
    p = cd // 2
b = n % 100
n = n // 10**p
if cd % 2 == 0:
    c = n % 100
    a = n // 100
    d1 = c // 100
    d2 = c % 10
else:
    c = n % 10
    a = n // 10
    d1 = c
    d2 = c
y = (d1 * 10 ** p + a)*10**p + b
y = y*10+d2
print(y)

