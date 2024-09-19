# PAR IMPAR DESCOMPOSICION SEPARA UN LADO PARES Y OTRO IMPARES
import math
n = int(input("Intro n:"))
cd = int(math.log10(n))+1
a = 0
b = 0
while n != 0:
    d = n // 10**(cd - 1)
    n = n % 10**(cd - 1)
    cd = cd - 1
    if d % 2 == 0:
        a = a * 10 + d
    else:
        b = b * 10 + d
print("PAR=", a, "IMPAR=", b)
