from functools import reduce
import operator

x = map(int, input().split())
total = reduce(operator.mul, x, 1)
print(total)
