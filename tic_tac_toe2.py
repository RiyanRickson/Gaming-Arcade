import random
def tic_game():
    board = [" " for _ in range(9)]

    def print_board():
        print("\n")
        for i in range(3):
            print(" | ".join(board[i*3:(i+1)*3]))
            if i < 2:
                print("---------")
        print("\n")

    def check_winner(player):
        win_conditions = [
            [0,1,2],[3,4,5],[6,7,8],  # rows
            [0,3,6],[1,4,7],[2,5,8],  # columns
            [0,4,8],[2,4,6]           # diagonals
        ]
        for cond in win_conditions:
            if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
                return True
        return False

    def check_draw():
        return " " not in board

    def player_move():
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move in range(9) and board[move] == " ":
                    board[move] = "X"
                    break
                else:
                    print("Invalid move, try again!")
            except ValueError:
                print("Enter a number between 1-9.")

    def computer_move():
        available_moves = [i for i, spot in enumerate(board) if spot == " "]
        move = random.choice(available_moves)
        board[move] = "O"
        print(f"Computer chose position {move+1}")

    # Main game loop
    print("* Tic-Tac-Toe: You (X) vs Computer (O) *")
    print_board()

    while True:
        player_move()
        print_board()
        
        if check_winner("X"):
            print("🎉 You win!")
            break
        if check_draw():
            print("It's a draw!")
            break

        computer_move()
        print_board()

        if check_winner("O"):
            print("🤖 Computer wins!")
            break
        if check_draw():
            print("It's a draw!")
            break