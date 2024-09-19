# ENCONTRAR EL DIGITO MAYOR Y MENOR
n = int(input("Intro n:"))
may = 0
men = 9
while n != 0:
    d = n % 10
    n = n // 10
    if d > may:
        may = d
    if d < men:
        men = d
print("Mayor=", may, "Menor=", men)
