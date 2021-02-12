n, d = map(int, input().split())

arr = list(map(int, input().split()))
cnt = 0

# sorted(arr)
for i in range(n):
    for j in range(i+1, n):
        if abs(arr[j] - arr[i]) <= d:
            cnt += 1

print(cnt*2)
