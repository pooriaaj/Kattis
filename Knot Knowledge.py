n = int(input())
m = set(map(int, input().split()))
p = set(map(int, input().split()))
difference = m - p
print("".join(map(str, sorted(difference))))
