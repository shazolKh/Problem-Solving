from collections import Counter
n = int(input())
a = []

for i in range(n):
    a.append(input())
cnt = Counter(a)
maxf = 0
ans = ''

for i in cnt:
    if cnt[i] > maxf:
        ans = i
        maxf = cnt[i]
print(ans)