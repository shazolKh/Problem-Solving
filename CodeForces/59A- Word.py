text = input()

upper, lower = 0, 0

for i in text:
    if 'a' <= i <= 'z':
        lower += 1
    elif 'A' <= i <= 'Z':
        upper += 1

if lower > upper or lower == upper:
    print(text.lower())
else:
    print(text.upper())
