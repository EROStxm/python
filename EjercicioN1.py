
def fact(w):
    f = 1
    for i in range(1, w+1, 1):
        f = f * i
    return f

def fibo(w):
    a = -1; b = 1; c = 0
    for i in range(1, w+1, 1):
        c = a + b
        a = b
        b = c
    return c
def clasica(w):
    p = 1; t = 1
    k=0
    for i in range(1, w+1, 1):
        k = t
        p = p + 1
        if p > t:
            p = 1
            t = t + 1
    return k
def SubBaj(w):
    t = 1; p = 1; sig = 1
    k=0
    for i in range(1,w+1,1):
        k = t
        t = t + sig
        p = p + 1
        if p > 2:
            sig = sig *(-1)
            p = 1
    return k

n = int(input("Intro n: "))
x = int(input("Intro x: "))
s = 0
for i in range(1, n+1, 1):
    s = s+(x**fact(fibo(i))/fact(clasica(i))**SubBaj(i))
    print(x, "^", fibo(i), "!/", clasica(i), "!^", SubBaj(i))
print("Total = ", s)
