import math

x, y, z = map(int, input().split())
boxDiagonal = math.sqrt(y ** 2 + z ** 2)

for _ in range(x):
    n = int(input())
    print("DA" if n <= boxDiagonal else "NE")
