n = int(input())
s = {int(input()) for _ in range(n)}
m = max(s)
missing = [x for x in range(1, m + 1) if x not in s]
if missing:
    print("\n".join(map(str, missing)))
else:
    print('good job')
