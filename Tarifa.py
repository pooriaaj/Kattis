allowed_megabytes = int(input())
months = int(input())

total_spent = sum(int(input()) for _ in range(months))
total_available = allowed_megabytes * (months + 1)
remained_megabytes = total_available - total_spent

print(remained_megabytes)
