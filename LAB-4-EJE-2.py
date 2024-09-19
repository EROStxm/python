n = int(input("Intro n:"))
k = int(input("Intro k:"))
if n == k:
    a = k * 2 ; b = a + k
else:
    if n < k:
        a = k ; b = a + k
    else:
        if n % k == 0:
            a = n - k ; b = n + k
        else:
            r = n % k ; a = n - r ; b = a + k
print(a, b)