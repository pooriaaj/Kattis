width = int(input())
pieces = int(input())
s = 0
for _ in range(pieces):
    newWidth, newHeight = map(int, input().split())
    s += newWidth * newHeight
print(int(s / width))
