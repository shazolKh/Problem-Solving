chess = []
for i in range(8):
    chess.append(input())
r = [1] * 8
c = [1] * 8
for i in range(8):
    for j in range(8):
        if chess[i][j] == 'W':
            r[i], c[j] = 0, 0
ans = 0
for i in range(8):
    ans += r[i] + c[i]
if ans == 16:
    print(8)
else:
    print(ans)
