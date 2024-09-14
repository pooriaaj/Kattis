won = set()
lis = []
for _ in range(int(input())):
    s = input()
    if len(won) == 12:
        continue
    a, _ = s.split()
    if a not in won:
        lis.append(s)
        won.add(a)
print('\n'.join(lis))
