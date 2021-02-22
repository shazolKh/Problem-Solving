n = int(input())

for i in range(n//4+1):
    result = n - 4 * i
    if result % 7 == 0:
        x = result // 7
        print('4' * i + '7' * x)
        exit()

print('-1')
