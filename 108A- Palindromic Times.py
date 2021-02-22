hh, mm = map(int, input().split(':'))
# m, n = 0, 0

# print(a, b)
while ((hh % 10) * 10 + (hh / 10)) != mm:
    mm += 1
    if mm == 60:
        hh += 1
        mm = 0

    if hh == 24:
        hh = 0

print(str(hh) + ':' + str(mm))