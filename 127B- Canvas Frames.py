from collections import Counter
n = int(input())
a = list(map(int, input().split()))

cnt = 0
v = Counter(a)
k = 0

for i in v:
    cnt += v[i] // 2

print(cnt // 2)
