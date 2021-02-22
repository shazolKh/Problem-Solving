n = int(input())
p = []
g = 0
for i in range(n):
    p.append(int(input()))
    
for i in range(n):
    c = 0
    while i >= 0:
        i = p[i] - 1
        c += 1
    g = max(g, c)
print(g)
