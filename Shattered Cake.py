width = int(input()); pieces = int(input()); print(int(sum(map(lambda x: x[0] * x[1], (map(int, input().split()) for _ in range(pieces)))) / width))
