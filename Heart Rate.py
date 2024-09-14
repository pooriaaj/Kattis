n = int(input()); [print(f'{(60 * x) / y - 60 / y:.4f} {(60 * x) / y:.4f} {(60 * x) / y + 60 / y:.4f}') for x, y in (map(float, input().split()) for _ in range(n))]
