probs = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
hotels = int(input())
spaces = map(lambda x: probs[int(x) - 2], input().split())
chance = sum(spaces)
print(chance / 36)
