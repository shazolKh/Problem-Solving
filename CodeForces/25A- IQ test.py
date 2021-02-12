n = int(input())
num = list(map(int, input().split()))
count = 0
total = 0
a = 0
b = 0

# for i in range(n):
#     num.append(map(int, input().split()))
#     # num.append(int(input()))

for i in range(n):
    if num[i] % 2 == 0:
        count += 1
    else:
        a = i

if count >= 2:
    print(a+1)
else:
    for i in range(n):
        if num[i] % 2 != 0:
            total += 1
        else:
            b = i

if total >= 2:
    print(b+1)