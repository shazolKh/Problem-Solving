key = []
for i in range(3):
    key.append(input())
if key[0][0] == key[2][2] and key[0][1] == key[2][1] and key[0][2] == key[2][0] and key[1][0] == key[1][2]:
    print('YES')
else:
    print('NO')