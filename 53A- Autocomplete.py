s, n = input(), int(input())
out = ''
for i in range(n):
    x = input()
    if x.find(s) == 0:
        if out == '':
            out = x
        else:
            out = min(out, x)
print(max(out, s))
