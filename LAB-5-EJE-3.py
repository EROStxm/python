n = int(input("Intro n: "))
k = int(input("Intro k: "))
a = int(input("Intro a: "))
b = int(input("Intro b: "))
t = a
c = a + b
for i in range(1, n+1):
    print(t,end=" ")
    if i % k == 0:
        t = c - t
