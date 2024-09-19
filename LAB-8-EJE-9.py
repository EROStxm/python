# DADO UN NUMERO CAMBIAR EL DIGITO PAR MENOR POR EL DIGITO IMPAR MAYOR
n = int(input("Intro n:"))
y = 0
po = 1
m1 = 0
m2 = 9
x = n
while n != 0:
    d = n % 10
    n = n // 10
    if d % 2 == 0:
        if d < m2:
            m2 = d
    else:
        if d > m1:
            m1 = d
while x != 0:
    d = x % 10
    x = x // 10
    if d % 2 == 0:
        if d == m2:
            d = m1
    else:
        if d == m1:
            d = m2
    y = d * po + y
    po = po * 10
print("Nuevo digito=", y)