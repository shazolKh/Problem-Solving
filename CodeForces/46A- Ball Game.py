n = int(input())

a = 2
for i in range(n-1):
    if a <= n:
        print(a, end=' ')
    else:
        if (a-n) % n == 0:
            print(n, end=' ')
        else:
            print((a-n) % n, end=' ')

    a = a+i+2
