n = float(input())
x = int(input())
total_area = 0
for _ in range(x):
    w, h = map(float, input().split())
    total_area += w * h
final_sum = total_area * n
print(final_sum)
