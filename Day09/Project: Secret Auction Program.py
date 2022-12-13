from logo import logo

print(logo)

print("Welcome to the secret auction program.")

should_end = False
players = {}

while not should_end:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))

    players[name] = bid

    bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n")

    if bidders == "no":
        should_end = True
        print(players)
        winner = max(players, key=players.get)

        print(f"The winner is {winner} with a bid of ${players[winner]}")
