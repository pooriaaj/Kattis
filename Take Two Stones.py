def game_outcome(stones):
    if stones % 2 == 0:
        return "Second player wins"
    else:
        return "First player wins"
stones = int(input("Enter the number of stones: "))
print(game_outcome(stones))
