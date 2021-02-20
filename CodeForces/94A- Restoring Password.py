n = input()
pas = []
ans = ''

for i in range(10):
    pas.append(input())

for i in range(0, 80, 10):
    ans += str(pas.index(n[i:i+10]))

print(ans)
