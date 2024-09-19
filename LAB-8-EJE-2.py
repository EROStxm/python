# DESCOMPOSICION DE IZQUIERDA A DERECHA
import math
n = int(input("Intro n:"))
cd = int(math.log10(n))+1
while cd != 0:
    d = n // 10**(cd-1)
    n = n % 10**(cd-1)
    cd = cd - 1
    print(d, end=" ")
