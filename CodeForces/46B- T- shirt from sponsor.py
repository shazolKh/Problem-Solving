def nex(p):
    if p == 'L':
        return ['L', 'XL', 'M', 'XXL', 'S']
    elif p == 'XL':
        return ['XL', 'XXL', 'L', 'M', 'S']
    elif p == 'S':
        return ['S', 'M', 'K', 'XL', 'XXL']
    elif p == 'M':
        return ['M', 'L', 'S', 'XL', 'XXL']
    elif p == 'XXL':
        return ['XXL', 'XL', 'L', 'M', 'S']


a = list(map(int, input().split()))
d = {}
d['S'] = a[0]
d['M'] = a[1]
d['L'] = a[2]
d['XL'] = a[3]
d['XXL'] = a[4]

q = int(input())
for _ in range(q):
    p = input()
    l = nex(p)
    for i in l:
        if d[i]:
            d[i] -= 1
            print(i)
            break
