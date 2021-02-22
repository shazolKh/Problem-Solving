prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

m, n = map(int, input().split())
f = False
for i in range(len(prime)):
    if prime[i] == m and prime[i+1] == n:
        f = True

# print(m, n, f)
if f:
    print('YES')
else:
    print('NO')
