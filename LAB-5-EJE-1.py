# 1,1,0,0,1,1,0,0,1,1,0,0,1,1....
n = int(input("Intro n: "))
t = 0
for i in range(1, n+1):
    print(t,end=" ")
    if i % 2 == 0:
        t = 1 - t
