def last_digit_of_factorial(m):
    if m == 0 or m == 1:
        return 1
    if m >= 10:
        return 0  # Factorials of numbers 10 and above end with 0
    last_digit = 1
    for i in range(2, m + 1):
        last_digit = (last_digit * i) % 10
    return last_digit

n = int(input())
for _ in range(n):
    m = int(input())
    print(last_digit_of_factorial(m))
