room = {}
traffic = 0
while 1:
    try:
        s = input()
    except EOFError:
        break
    if s[0] == '+':
        room[s[1:]] = None
    elif s[0] == '-':
        room.pop(s[1:])
    else:
        traffic += len(s.split(':')[1]) * len(room)
print(traffic)