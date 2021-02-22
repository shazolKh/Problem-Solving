m = input()
n = input()
li = []
if len(m) == len(n):
    # a = int(m)
    # b = int(n)
    for i in range(len(m)):
        if m[i] == n[i]:
            li.append('0')
        else:
            li.append('1')
    # a = str(li)
    # print(a)
    print(''.join(li))
