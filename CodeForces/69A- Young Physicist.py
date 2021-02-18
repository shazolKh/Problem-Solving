n = int(input())

x1 = x2 = x3 = 0

for i in range(n):
    x, y, z = map(int, input().split())

    x1 += x
    x2 += y
    x3 += z
if x1 == x2 == x3 == 0:
    print('YES')
else:
    print('NO')
