n = int(input()); m = list(map(int, input().split())); print(sum(i for i in m if i >= 0) / sum(1 for i in m if i >= 0))
