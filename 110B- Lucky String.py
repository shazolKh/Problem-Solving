n = int(input())

for i in range(n):
    if i % 4 == 0:
        print('a', end='')
    if i % 4 == 1:
        print('b', end='')
    if i % 4 == 2:
        print('c', end='')
    if i % 4 == 3:
        print('d', end='')
