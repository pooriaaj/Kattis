n = int(input()); [print('skipped') if (cases := input()) == 'P=NP' else print(sum(map(int, cases.split('+')))) for _ in range(n)]
