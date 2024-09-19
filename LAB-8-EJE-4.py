# COMPOSICION A LA IZQUIERDA A DERECHA
n = int(input("Intro n:"))
y = 0
po = 1
for i in range(1, n+1):
    d = int(input("Intro d:"))
    y = d * po + y
    po = po * 10
print(y)
