s = input()

if '4' not in s and '7' not in s:
    print(-1)
    exit()
elif s.count('4') >= s.count('7'):
    print('4')
else:
    print(7)
