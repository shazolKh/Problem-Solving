n = input()

total = 0
count = 0

while int(n) > 9:
    for i in range(len(n)):
        total += int(n[i])

    count += 1
    n = str(total)
    total = 0
print(count)
