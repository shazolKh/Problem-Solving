n = input()
m = input()

n1 = n.replace('0', '')
m1 = m.replace('0', '')

# print(n1, m1)

n2 = int(n)
m2 = int(m)
n11 = int(n1)
m11 = int(m1)

in_sum = str(n2 + m2)
z_sum = str(n11 + m11)

# print(in_sum, z_sum)

if in_sum.replace('0', '') == z_sum:
    print('YES')
else:
    print('NO')
