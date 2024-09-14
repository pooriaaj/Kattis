probabilities = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
num_hotels = int(input())
space_indices = set(map(int, input().split()))
total_chance = sum(probabilities[index - 2] for index in space_indices)
print(total_chance / 36)
