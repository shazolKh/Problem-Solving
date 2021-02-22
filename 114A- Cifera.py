# a, b = map(int, input().split())
a = int(input())
b = int(input())
i = 0
while a ** i < b:
    i += 1

if b == a ** i:
    print("YES")
    print(i - 1)
else:
    print("NO")