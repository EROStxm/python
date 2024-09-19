a = -1
b = 1
c = a+b
x = int(input("Intro x:"))
while x!=1:
    if x == c:
        print(x)
        a = b
        b = c
        x = int(input("Intro x:"))
