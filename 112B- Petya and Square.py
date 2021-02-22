n, x, y = map(int, input().split())

n //= 2

if (x == n or x == n+1) and (y == n or y == n + 1):
    print('NO')
else:
    print('YES')
