def findGCD(x, y):
    if x % y == 0:
        return y
    return findGCD(y, x % y)


a, b = map(int, input().split())

c = max(a, b)

no_of_possibility = 6 - c + 1

x = findGCD(no_of_possibility, 6)

print(str(no_of_possibility // x) + "/" + str(6 // x))
