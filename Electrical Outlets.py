n = int(input())
for _ in range(n):
    num = input()
    numbers = num.split()
    total_sum = sum(int(numbers[j]) for j in range(1, len(numbers)))
    print(total_sum + 1 - int(numbers[0]))
