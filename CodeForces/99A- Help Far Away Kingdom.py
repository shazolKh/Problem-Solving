n = input()

a = n.index('.')
b = int(n[:a])
c = int(n[a + 1])

if n[a - 1] == '9':
    print('GOTO Vasilisa.')
elif c <= 4:
    print(b)
else:
    print(b + 1)

