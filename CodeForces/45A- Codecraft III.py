months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

m = input()
n = int(input())
q = months.index(m)
# print(q)
r = (q + n) % 12
print(months[r])

