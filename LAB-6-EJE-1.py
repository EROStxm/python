#1 2 3 4 5 4 3 2 1 2 3 4 5 4 3 2 1
n = int(input("Intro n: "))
t = 1
p = 1
sig = 1
for i in range(1, n+1):
    print(t, end=" ")
    t = t + sig
    p = p + 1
    if p > 4:
        sig = sig * -1
        p = 1