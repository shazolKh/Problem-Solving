n = int(input())
k = 0

for i in range((n * 2) + 1):
    t = 0
    for j in range((n*2) + 1):
        if n-k <= j <= n+k:
            if j < n + k:
                print(t, end=' ')
            else:
                print(t, end='')
            if j < n:
                t += 1
            else:
                t -= 1
            if j == n + k:
                break
        else:
            print(' ', end=' ')

    if i < n:
        k += 1
    else:
        k -= 1
    print('')
