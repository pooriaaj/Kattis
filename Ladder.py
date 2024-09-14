import math

height, angle = map(int, input().split())
radians = math.radians(angle)
ladderheight = math.ceil(height / math.sin(radians))
print(ladderheight)
