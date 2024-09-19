def recursivoFat(n):
    if n == 0:
        return 1
    else:
        return (n*recursivoFat(n-1))
n = int(input("Intro n: "))
print("Total = ", recursivoFat(n))
