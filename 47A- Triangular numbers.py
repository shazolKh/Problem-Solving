n = int(input())
f = 0

for i in range(1, n+1):
    if (i*(i+1)) // 2 == n:
        print('YES')
        f = 1
        break
if f == 0:
    print('NO')


