n = int(input())
s = 0
for _ in range(n):
    names = input().lower()
    if 'rose' in names or 'pink' in names:
        s += 1
if s == 0:
    print('I must watch star wars with my daughter')
else:
    print(s)
