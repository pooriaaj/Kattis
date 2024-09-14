classes, available_bottles = map(int, input().split())
empty = 0
for _ in range(classes):
    bottles_needed = int(input())
    empty += bottles_needed
print('jebb' if empty <= available_bottles else 'Neibb')
