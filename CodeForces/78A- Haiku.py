count = 0
a = input()
b = input()
c = input()
v1, v2, v3 = 0, 0, 0

for i in a:
    if i in 'aeiou':
        v1 += 1
for i in b:
    if i in 'aeiou':
        v2 += 1
for i in c:
    if i in 'aeiou':
        v3 += 1

# print(v1, v2, v3)
if v1 == 5 and v2 == 7 and v3 == 5:
    print('YES')
else:
    print('NO')
