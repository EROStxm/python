# X**1 , X**2,X**3,X**4,X**5.........
n = int(input("Intro n:"))
x = int(input("Intro x:"))
s = 0
for i in range(1, n+1):
    s = s + x**i
    print(x, "^", i, end="+ ")
print("Total es= ", s)
