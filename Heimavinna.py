n = input()
s = 0
if ';' in n:
    ranges = n.split(';')
    for r in ranges:
        if '-' in r:
            start, end = map(int, r.split('-'))
            s += end - start + 1
        else:
            s += 1
elif '-' in n:
    start, end = map(int, n.split('-'))
    s += end - start + 1
else:
    s += 1

print(s)
