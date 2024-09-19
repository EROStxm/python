# SERIE 1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7..........
n = int(input("Intro n: "))
p = 1
t = 1
for i in range(1, n+1):
    print(t, end=" ")
    p = p + 1
    if p > t:
        t = t + 1
        p = 1
