n = [input() for _ in range(5)]
if sum(row.count('k') for row in n) != 9:
    print('invalid')
else:
    moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (-2, 1), (2, 1), (2, -1), (-2, -1)]
    for i in range(5):
        for j in range(5):
            if n[i][j] == 'k' and any(0 <= i + k < 5 and 0 <= j + l < 5 and n[i + k][j + l] == 'k' for k, l in moves):
                print('invalid')
                exit(0)
    print('valid')
