#Dado un numero de 6 digitos eliminar el   digito que representa la decena
n = int(input("Intro n: "))
b = n % 10
a = n // 100
c = a * 10 + b
print("nuevo num= ", c)
