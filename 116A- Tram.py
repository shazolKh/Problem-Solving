n = int(input())
c = 0
max1 = 0
for _ in range(n):
    a, b = map(int, input().split())
    c = c - a + b
    max1 = max(max1, c)
print(max1)
