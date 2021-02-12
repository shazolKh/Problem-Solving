n, m = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)

i = 0
ans = 0

while i < m and a[i] < 0:
    ans += a[i]
    i += 1
print(abs(ans))