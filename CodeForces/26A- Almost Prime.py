n = int(input())
c = 0
for i in range(1, n+1):
    x = i
    y = 0
    for j in range(2, x+1):
        f = 0
        while x % j == 0:
            x //= j
            f = 1
        if f:
            y += 1
    if y == 2:
        c += 1
print(c)