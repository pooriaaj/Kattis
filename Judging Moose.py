a, b = map(int, input().split())
if a > b and a != b:
    print('odd', a * 2)
elif a < b and a != b:
    print('odd', b * 2)
elif a == b and a != 0:
    print('even', a * 2)
else:
    print('Not a moose')
