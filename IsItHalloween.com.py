print((lambda m,d: 'yup' if (m.startswith('O') and d == '31') or (m.startswith('D') and d == '25') else 'nope')(*input().split()))
