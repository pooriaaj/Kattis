x, y = map(int, input().split()); print(x + 1) if x == y else print('\n'.join(map(str, range(y + 1, x + 2)))) if x > y else print('\n'.join(map(str, range(x + 1, y + 2))))
