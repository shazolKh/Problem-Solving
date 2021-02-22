MOD, cost = 10 ** 9 + 7, 0
frac = [0] * 200002


def C(m, n):
    ans2 = frac[m]
    ans2 = ans2 * pow(frac[n], MOD - 2, MOD) % MOD
    ans2 = ans2 * pow(frac[m - n], MOD - 2, MOD) % MOD
    return ans2


frac[0] = 1
for i in range(1, 200002):
    frac[i] = frac[i - 1] * i % MOD
h, w, n = map(int, input().split())
spot, dp = [[0] * 2 for i in range(n)], [[0] * 2 for i in range(n)]
for i in range(n):
    spot[i][0], spot[i][1] = map(int, input().split())
spot.sort()
for i in range(n):
    if i == 0:
        dp[0] = C(spot[0][0] - 1 + spot[0][1] - 1, spot[0][1] - 1)
    else:
        cost = 0
        for i2 in range(i):
            if spot[i2][1] <= spot[i][1]:
                cost = (cost + dp[i2] * C(spot[i][0] - spot[i2][0] + spot[i][1] - spot[i2][1],
                                          spot[i][1] - spot[i2][1])) % MOD
        dp[i] = (C(spot[i][0] - 1 + spot[i][1] - 1, spot[i][1] - 1) - cost + MOD) % MOD
ans = C(h - 1 + w - 1, h - 1) % MOD
for i in range(n):
    ans = (ans - dp[i] * C(h - spot[i][0] + w - spot[i][1], w - spot[i][1])) % MOD
print(ans)
