cells = int(input())
lanes = int(input())
empty = 0

for _ in range(lanes):
    row = input()
    empty += row.count('.')

total_cells = cells * lanes
print(f'{empty / total_cells:.3f}')
