import math

n, k = map(int, input().split())
r = 0
li = [[]for i in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    li[i].append(x)
    li[i].append(y)

for i in range(n-1):
    r += math.sqrt(pow(li[i+1][0] - li[i][0], 2) + pow(li[i+1][1]-li[i][1], 2))
r *= k
print(r/50)
