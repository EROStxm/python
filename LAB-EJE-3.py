#Dado un numero de 5 digitos eliminar el central
n = int(input("Intro n: "))
a = n // 1000
b = n % 100
c = a * 100 + b
print("nuevo num= ", c)
