count_cards, secret_prediction, steps = map(int, input().split())
for _ in range(steps):
    m, *chosen_cards = map(int, input().split())
    print('KEEP' if secret_prediction in chosen_cards else 'REMOVE')
