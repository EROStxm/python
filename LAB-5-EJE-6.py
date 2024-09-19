#GENERALIZANDO EL EJERCICIO N°5
n = int(input("Intro n: "))
a = int(input("Intro a: "))
b = int(input("Intro b: "))
p = 1
t = a
z = a+b
for i in range(1, n+1):
    print(t, end=" ")
    p = p + 1
    if p > t:
        t = z - t
        p = 1
