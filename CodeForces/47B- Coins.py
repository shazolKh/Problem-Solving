a, b, c = 0, 0, 0
for i in range(3):
    s = input()

    if s[1] == '>':
        if s[0] == 'A':
            a += 1
        elif s[0] == 'B':
            b += 1
        else:
            c += 1

    else:
        if s[2] == 'A':
            a += 1
        elif s[2] == 'B':
            b += 1
        else:
            c += 1

if a < b < c:
    print('ABC')
elif a < c < b:
    print('ACB')
elif b < a < c:
    print('BAC')
elif b < c < a:
    print('BCA')
elif c < a < b:
    print('CAB')
elif c < b < a:
    print('CBA')
else:
    print('Impossible')
