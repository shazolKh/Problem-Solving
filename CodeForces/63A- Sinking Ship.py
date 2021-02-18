n = int(input())
l1 = []
l2 = []
l3 = []
l4 = []

for i in range(n):
    s = input().split()

    if s[1] == 'woman' or s[1] == 'child':
        l1.append(s[0])
    elif s[1] == 'man':
        l2.append(s[0])
    elif s[1] == 'captain':
        l3.append(s[0])
    else:
        l4.append(s[0])
l5 = l4 + l1 + l2 + l3

for i in range(n):
    print(l5[i])