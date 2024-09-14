required = [1, 1, 2, 2, 2, 8]
current = map(int, input().split())

for req, cur in zip(required, current):
    print(req - cur)
