from re import match

flag = input()
p1 = input()
p2 = input()

pattern = '.*' + p1 + '.*' + p2 + '.*'
forward = match(pattern, flag) is not None
backward = match(pattern, flag[::-1]) is not None

if forward and backward:
    print('both')
elif forward:
    print('forward')
elif backward:
    print('backward')
else:
    print('fantasy')