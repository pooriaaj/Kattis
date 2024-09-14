n = int(input())
books_prices = sorted([int(input()) for _ in range(n)], reverse=True)
total = sum(books_prices[i] for i in range(n) if (i + 1) % 3 != 0)
print(total)
