a, b, c = sorted(map(int, input().split()))
letters = input()
mapping = {'A': a, 'B': b, 'C': c}
print(' '.join(str(mapping[l]) for l in letters))
