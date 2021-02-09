n = int(input())
d = int(input())
seq = []

for i in range(n):
    seq.append(int(input()))
prev = seq[0] - 1
moves = 0
for s in seq:
    if s <= prev:
        m = (prev - s) / d + 1
        moves += m
        prev = s + d * m
    else:
        prev = s
print(moves)
