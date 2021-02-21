n = int(input())
c = list(map(int, input().split()))
k = 0
for i in range(n):
    k += (c[i] - 1) * (i + 1) + 1
print(k)
