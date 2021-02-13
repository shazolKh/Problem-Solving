n = int(input())
d = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
print(d[a-1]+sum(d[a:b-1]))