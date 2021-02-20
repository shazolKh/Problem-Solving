m, n = list(map(int, input().split()))

f = True
while f:
    for i in range(1, m+1):
        if i <= n:
            n -= i
        else:
            f = False
            break
print(n)
