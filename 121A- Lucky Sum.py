l, r = map(int, input().split())
s = 0

for i in range(l, r + 1):
    n = list(str(i))
    for j in range(len(n)):
        if n[j] == '4' or n[j] == '7':
            continue
        elif n[j] < '4':
            n[j] = '4'
        elif n[j] < '7':
            n[j] = '7'
        else:
            n[j] = '44'
    s += int(''.join(n))
print(s)
