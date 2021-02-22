n, t = map(int, input().split())
di = {}

for i in range(n):
    x, a = map(int, input().split())
    di[x] = a

ans = 2
lis = di.keys()
sorted(lis)
pre = -(1 << 30)

for k in lis:
    a = float(di[k])/2
    if pre != -(1 << 30):
        dis = abs((k-a) - pre)
        if dis > t:
            ans += 2
        elif dis == t:
            ans += 1
    pre = k + a
print(ans)