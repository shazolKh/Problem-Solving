n = int(input())
li = list(map(int, input().split()))

s = sum(li)
way = 0
x = li[way]
for i in range(1, n):
    if s-x == x:
        way += 1
    x += li[i]
print(way)
