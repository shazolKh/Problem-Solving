# alcohol = ['ABSINTH', 'BEER', 'BRANDY', 'CHAMPAGNE', 'GIN', 'RUM', 'SAKE', 'TEQUILA', 'VODKA', 'WHISKEY', 'WINE']
#
# n = int(input())
# c = 0
# s = []
# for i in range(n):
#     s.append(input())
# if set(s) & set(alcohol):
#     c += 1
# for i in range(len(s)):
#     if s[i].isdigit():
#         if int(s[i]) < 18:
#             c += 1
# print(c)

alcohol = ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"]
n = int(input())
c = 0
for _ in range(n):
    s = input()
    if s in alcohol:
        c = c+1
    if s.isdigit():
        if int(s) < 18:
            c = c+1
print(c)
