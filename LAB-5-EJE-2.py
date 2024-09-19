n = int(input("Intro n: "))
k = int(input("Intro k: "))
t = 0
for i in range(1, n+1):
    print(t,end=" ")
    if i % k == 0:
        t = 1 - t
