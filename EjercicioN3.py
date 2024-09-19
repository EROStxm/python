def recursivoPotencia(x,y):
    if y == 0:
        return 1
    else:
        return (x*recursivoPotencia(x,y-1))

x = int(input("Intro x: "))
y = int(input("Intro y: "))
print("Total = ",recursivoPotencia(x,y))
