n, P1, P2, P3, T1, T2 = map(int, input().split())
period = []
for i in range(n):
    period.append(map(int, input().split()))
cur = period[0][0]
consumption = 0
for p in period:
    t = min(p[0] - cur, T1)
    cur += t
    consumption += P1 * t

    t = min(p[0] - cur, T2)
    cur += t
    consumption += P2 * t

    t = p[0] - cur
    cur += t
    consumption += P3 * t

    consumption += (p[1] - p[0]) * P1
    cur = p[1]
print(consumption)
