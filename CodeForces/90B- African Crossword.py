n, m = map(int, input().split())
s = [input() for i in range(n)]
ans = ""
for i in range(n):
    for j in range(m):
        if s[i][j] in s[i][:j] + s[i][j + 1:]:
            continue
        c = 0
        for x in range(n):
            if s[x][j] == s[i][j]:
                c += 1
        if c == 1:
            ans += s[i][j]
print(ans)
