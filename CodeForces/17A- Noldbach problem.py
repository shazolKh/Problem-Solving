from math import sqrt

n, k = map(int, input().split())
prime = []


def isPrime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def getPrime():
    for i in range(3, 1100):
        if isPrime(i):
            prime.append(i)


def isOk(x):
    if prime.count(x) != 0:
        for j in range(prime.index(x)+1):
            if x-1 == prime[j]+prime[j+1]:
                return True
    return False


def getAns():
    cnt =0
    getPrime()
    for i in range(3, n+1):
        if isOk(i):
            cnt += 1
    if cnt >= k:
        return 'YES'
    return 'NO'


print(getAns())
