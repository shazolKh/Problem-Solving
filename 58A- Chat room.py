n = input()
text = 'hello'
i = 0

for j in n:
    if i < len(text) and j == text[i]:
        i += 1

if i == 5:
    print('YES')
else:
    print('NO')
