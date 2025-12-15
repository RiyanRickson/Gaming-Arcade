import random
def slotgame():
    def spin_row():
        symbols = ['🌺', '🌻', '🌼', '🌹']
        results = []
        for _ in range(3):
            results.append(random.choice(symbols))
        return results

    def print_row(row):
        print(" | ".join(row))

    def get_payout(row, bet):
        if row[0] == row[1] == row[2]:   # All 3 symbols match
            if row[0] == '🌺':
                return bet * 10
            elif row[0] == '🌻':
                return bet * 20
            elif row[0] == '🌼':
                return bet * 30
            elif row[0] == '🌹':
                return bet * 40
        return 0

    
    balance = 100
    print("|*******************|")
    print("Welcome to Betting Game")
    print("Symbols: 🌺 🌻 🌼 🌹")
    print("|*******************|")

    while balance > 0:
        print(f"\nCurrent Balance: Rs{balance}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Balance")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("\nPROCESSING!!\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won Rs{payout}!")
        else:
            print("You Lost!")

        balance += payout
        if not input("Play again?(y/n): ").lower()=="y":
                break

    print("\nGame Over! You ran out of balance.")
    

