n = int(input())
a = [int(i) for i in input().split()]
d = sum(a)
e = 1
f = []

for i in range(0, len(a)):
    if a[i] % 2 != 0:
        f.append(a[i])

if len(f) == 0:
    print(0)
else:
    while e > 0:
        if d == 0:
            e = 0
        elif d % 2 == 0:
            d = d - min(f)
        else:
            e = 0
    print(d)
