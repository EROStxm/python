# SUMATORIA DE 1+2+3+4+5+6+7+8+9
n = int(input("Intro n:"))
s = 0
for i in range(1, n+1):
    s = s + i
    print(i, end="+ ")
print("Total es= ", s)
