n = int(input("Intro n: "))
p = 1
t = 2
z = 2+5
for i in range(1, n+1):
    print(t, end=" ")
    p = p + 1
    if p > t:
        t = z - t
        p = 1

