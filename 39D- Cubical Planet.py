a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

ans = (a1-a2)**2 + (b1-b2)**2 + (c1-c2)**2

if ans == 3:
    print('NO')
else:
    print('YES')
