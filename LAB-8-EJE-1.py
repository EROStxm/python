# DESCOMPOSICION DE DERECHA A IZQUIERDA
n = int(input("Intro n: "))
while n !=0:
    d = n % 10
    n = n // 10
    print(d, end=" ")
    