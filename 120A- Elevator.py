a, b = map(int, input().split())
ans = 2 * (b - 1)
for i in range(a):
    x, y, z = map(int, input().split())
    if x == y:
        print(z)
    elif x < y:
        if z < x:
            print(y - 1)
        else:
            print(ans * ((z + ans - x) // ans) + y - 1)
    else:
        k = b - 1
        x = b + 1 - x
        y = b + 1 - y
        z -= k
        if z < x:
            print(k + y - 1)
        else:
            print(k + ans * ((z + ans - x) // ans) + y - 1)
