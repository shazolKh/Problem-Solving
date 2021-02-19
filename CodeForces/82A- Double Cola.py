n = int(input())
ar = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
n -= 1
while n >= 5:
    n = n - 5
    n = n // 2
print(ar[n])
