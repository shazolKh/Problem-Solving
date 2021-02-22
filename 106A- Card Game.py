l = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
s = input()
x, y = input().split()
if (x[1] == s and x[1] != y[1]) or (x[1] == y[1] and l.index(x[0]) > l.index(y[0])):
    print("YES")
else:
    print("NO")