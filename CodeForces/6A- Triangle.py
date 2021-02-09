a = int(input())
b = int(input())
c = int(input())
d = int(input())
# while (int(a), int(b), int(c), int(d)):
if (a < b+c and b < a+c and c < a+b) | (a < b+d and b < a+d and d < a+b) | (a < d+c and d < a+c and c < a+d) |\
        (d < b+c and b < d+c and c < d+b):
    print('TRIANGLE')
elif (a == b + c | b == a + c | c == a + b) | (a == b + d | b == a + d | d == a + b) | \
        (a == d + c | d == a + c | c == a + d) | (d == b + c | b == d + c | c == d + b):
    print('SEGMENT')
else:
    print('IMPOSSIBLE')