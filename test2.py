import tkinter as tk
from tkinter import messagebox
import random
import ref  # uses your original cric dict from ref.py


# ========================= MAIN ARCADE WINDOW ========================= #

class GamingArcade(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gaming Arcade")
        self.geometry("600x480")
        self.resizable(False, False)

        title_label = tk.Label(self, text="Gaming Arcade", font=("Arial", 26, "bold"))
        title_label.pack(pady=20)

        subtitle = tk.Label(self, text="Choose a game to play!", font=("Arial", 12))
        subtitle.pack(pady=5)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=20)

        games = [
            ("Rock Paper Scissors", self.open_rps),
            ("Number Guessing", self.open_num_guess),
            ("Dice Roll", self.open_dice),
            ("Tic Tac Toe", self.open_tictac),
            ("Adventure Game", self.open_adventure),
            ("Cric Guesser", self.open_cric_guesser),
        ]

        for i, (text, cmd) in enumerate(games):
            b = tk.Button(btn_frame, text=text, width=25, height=2, command=cmd)
            b.grid(row=i, column=0, pady=5, padx=10, sticky="w")

        quit_btn = tk.Button(self, text="Exit", width=10, command=self.destroy)
        quit_btn.pack(pady=10)

    def open_rps(self):
        RPSWindow(self)

    def open_num_guess(self):
        NumberGuessWindow(self)

    def open_dice(self):
        DiceWindow(self)

    def open_tictac(self):
        TicTacToeWindow(self)

    def open_adventure(self):
        AdventureGameWindow(self)

    def open_cric_guesser(self):
        CricGuesserWindow(self)


# ========================= ROCK PAPER SCISSORS ========================= #

class RPSWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Rock Paper Scissors")
        self.geometry("400x300")
        self.resizable(False, False)

        self.choices = ["Rock", "Paper", "Scissors"]

        label = tk.Label(self, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
        label.pack(pady=10)

        self.result_label = tk.Label(self, text="Make your move!", font=("Arial", 12))
        self.result_label.pack(pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        for i, choice in enumerate(self.choices):
            b = tk.Button(btn_frame, text=choice, width=10,
                          command=lambda c=choice: self.play(c))
            b.grid(row=0, column=i, padx=5)

    def play(self, user_choice):
        comp_choice = random.choice(self.choices)
        if user_choice == comp_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        self.result_label.config(
            text=f"You: {user_choice} | Computer: {comp_choice}\n{result}"
        )


# ========================= NUMBER GUESSING ========================= #

class NumberGuessWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Number Guessing Game")
        self.geometry("400x300")
        self.resizable(False, False)

        self.target = random.randint(1, 100)
        self.attempts = 0

        label = tk.Label(self, text="Guess a number between 1 and 100", font=("Arial", 12))
        label.pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        guess_btn = tk.Button(self, text="Guess", command=self.check_guess)
        guess_btn.pack(pady=5)

        self.feedback = tk.Label(self, text="", font=("Arial", 11))
        self.feedback.pack(pady=10)

        reset_btn = tk.Button(self, text="Reset Game", command=self.reset_game)
        reset_btn.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.feedback.config(text="Please enter a valid integer.")
            return

        if guess < 1 or guess > 100:
            self.feedback.config(text="Number must be between 1 and 100.")
            return

        self.attempts += 1

        if guess < self.target:
            self.feedback.config(text="Too low! Try again.")
        elif guess > self.target:
            self.feedback.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Correct!", f"You guessed it in {self.attempts} attempts!")
            self.reset_game()

    def reset_game(self):
        self.target = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback.config(text="New number generated. Start guessing!")


# ========================= DICE ROLL ========================= #

class DiceWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Dice Roll")
        self.geometry("300x200")
        self.resizable(False, False)

        label = tk.Label(self, text="Dice Rolling Simulation", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        self.result_label = tk.Label(self, text="Click roll!", font=("Arial", 12))
        self.result_label.pack(pady=10)

        roll_btn = tk.Button(self, text="Roll Dice", width=12, command=self.roll)
        roll_btn.pack(pady=5)

    def roll(self):
        value = random.randint(1, 6)
        self.result_label.config(text=f"You rolled: {value}")


# ========================= TIC TAC TOE ========================= #

class TicTacToeWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Tic Tac Toe")
        self.geometry("320x360")
        self.resizable(False, False)

        self.current_player = "X"
        self.board = [None] * 9

        title = tk.Label(self, text="Tic Tac Toe (2 players)", font=("Arial", 14, "bold"))
        title.pack(pady=10)

        self.info_label = tk.Label(self, text="Player X's turn", font=("Arial", 12))
        self.info_label.pack(pady=5)

        self.btns = []
        grid_frame = tk.Frame(self)
        grid_frame.pack()

        for i in range(9):
            b = tk.Button(grid_frame, text="", width=5, height=2,
                          font=("Arial", 18),
                          command=lambda idx=i: self.handle_move(idx))
            b.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.btns.append(b)

        reset_btn = tk.Button(self, text="Reset Board", command=self.reset_board)
        reset_btn.pack(pady=10)

    def handle_move(self, idx):
        if self.board[idx] is not None:
            return

        self.board[idx] = self.current_player
        self.btns[idx].config(text=self.current_player)

        if self.check_winner(self.current_player):
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.reset_board()
            return

        if all(self.board):
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_board()
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.info_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self, player):
        wins = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        return any(self.board[a] == self.board[b] == self.board[c] == player for a, b, c in wins)

    def reset_board(self):
        self.board = [None] * 9
        for b in self.btns:
            b.config(text="")
        self.current_player = "X"
        self.info_label.config(text="Player X's turn")


# ========================= ADVENTURE GAME (GUI) ========================= #
# Based on Adventure_game.py story/choices.

class AdventureGameWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Adventure Game")
        self.geometry("600x400")
        self.resizable(False, False)

        self.state = "choice1"

        title = tk.Label(self, text="Spooky Night Adventure", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        self.text_label = tk.Label(
            self,
            text="",
            wraplength=560,
            justify="left",
            font=("Arial", 11),
        )
        self.text_label.pack(pady=15)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        self.choice1_btn = tk.Button(btn_frame, width=25, command=self.on_choice1)
        self.choice1_btn.grid(row=0, column=0, padx=5, pady=5)

        self.choice2_btn = tk.Button(btn_frame, width=25, command=self.on_choice2)
        self.choice2_btn.grid(row=0, column=1, padx=5, pady=5)

        self.restart_btn = tk.Button(self, text="Restart Adventure", command=self.restart)
        self.restart_btn.pack(pady=10)

        self.update_scene()

    def update_scene(self):
        if self.state == "choice1":
            self.text_label.config(
                text=(
                    "Welcome to our spooky adventure game!!\n\n"
                    "You are going to your home in a dark night and your car had some problem in a lonely road.\n"
                    "While you were analysing the situation another car came and stopped by to check on you.\n"
                    "He was an old man probabily in his 60s.\n"
                    "He offered you a lift and you have TWO choices:\n\n"
                    "ACCEPT it or REJECT it."
                )
            )
            self.choice1_btn.config(text="Accept the ride (yes)")
            self.choice2_btn.config(text="Reject the ride (no)")

        elif self.state == "death_trinity":
            self.text_label.config(
                text="He was the trinity killer and he killed you 💀 Game over!!"
            )
            self.choice1_btn.config(text="Play again")
            self.choice2_btn.config(text="Close")

        elif self.state == "walk_bear_intro":
            self.text_label.config(
                text=(
                    "You said no and now you're regretting your decision.\n\n"
                    "You decide to walk to the nearest gas station, it is 15 minutes away on foot.\n\n"
                    "Walking...\n"
                    "You see something like a bear but you're not sure.\n\n"
                    "You have two thoughts now:\n"
                    "1) Run faster silently\n"
                    "2) Walk at your usual speed ignoring the danger."
                )
            )
            self.choice1_btn.config(text="Run silently")
            self.choice2_btn.config(text="Ignore and keep walking")

        elif self.state == "after_run":
            self.text_label.config(
                text=(
                    "Running..... huh huh huh...\n"
                    "You see the gas station ahead.\n\n"
                    "You want something to drink and eat now after the bear event.\n"
                    "You see a diet coke and a redbull."
                )
            )
            self.choice1_btn.config(text="Choose Diet Coke")
            self.choice2_btn.config(text="Choose Redbull")

        elif self.state == "after_walk_ignore":
            self.text_label.config(
                text=(
                    "Walking.....\n"
                    "Oops!! You heard a bear's voice and started running...\n"
                    "You survived and saw the gas station.\n\n"
                    "You want something to drink and eat now after the bear event.\n"
                    "You see a diet coke and a redbull."
                )
            )
            self.choice1_btn.config(text="Choose Diet Coke")
            self.choice2_btn.config(text="Choose Redbull")

        elif self.state == "ride_offer_again":
            self.text_label.config(
                text=(
                    "You pick a drink and browse through the shop, thinking what to do next.\n"
                    "But then you see the SAME old man again. Looks like he is offering you a ride again.\n\n"
                    "Would you like to take the ride?"
                )
            )
            self.choice1_btn.config(text="Take the ride (yes)")
            self.choice2_btn.config(text="Book a cab instead (no)")

        elif self.state == "ride_no_cab":
            self.text_label.config(
                text=(
                    "You: 'Sorry, I booked a cab, it is gonna arrive soon.'\n\n"
                    "While you are checking out, the shopkeeper tells you to stay safe as a serial killer "
                    "is around hunting lonely people and tells a story which resembles your story with the old man tonight.\n\n"
                    "You now have two options:\n"
                    "1) Call the cops and tell the whole story.\n"
                    "2) Think of it just as a coincidence and go home via your cab."
                )
            )
            self.choice1_btn.config(text="Call the cops")
            self.choice2_btn.config(text="Ignore and leave")

        elif self.state == "home_safe":
            self.text_label.config(
                text="🎊 Woops, you reached home safely after one hell of a night! 🎊"
            )
            self.choice1_btn.config(text="Play again")
            self.choice2_btn.config(text="Close")

    def on_choice1(self):
        if self.state == "choice1":
            # Accept ride -> death
            self.state = "death_trinity"
        elif self.state == "death_trinity":
            self.state = "choice1"
        elif self.state == "walk_bear_intro":
            # Run silently
            self.state = "after_run"
        elif self.state in ("after_run", "after_walk_ignore"):
            # Choose drink (diet coke) -> same next state
            self.state = "ride_offer_again"
        elif self.state == "ride_offer_again":
            # Take the ride -> death
            self.state = "death_trinity"
        elif self.state == "ride_no_cab":
            # Call cops -> still reach home safely
            self.state = "home_safe"
        elif self.state == "home_safe":
            self.state = "choice1"

        self.update_scene()

    def on_choice2(self):
        if self.state == "choice1":
            # Reject ride -> walk & bear
            self.state = "walk_bear_intro"
        elif self.state == "death_trinity":
            self.destroy()
            return
        elif self.state == "walk_bear_intro":
            # Ignore danger
            self.state = "after_walk_ignore"
        elif self.state in ("after_run", "after_walk_ignore"):
            # Choose drink (redbull) -> same next state
            self.state = "ride_offer_again"
        elif self.state == "ride_offer_again":
            # Book a cab
            self.state = "ride_no_cab"
        elif self.state == "ride_no_cab":
            # Ignore & leave -> also safe in original logic
            self.state = "home_safe"
        elif self.state == "home_safe":
            self.destroy()
            return

        self.update_scene()

    def restart(self):
        self.state = "choice1"
        self.update_scene()


# ========================= CRIC GUESSER (GUI) ========================= #
# Based closely on Cric_guesser.py behaviour:
# - role + country selection builds key like "11", "22" etc.
# - picks from ref.cric[c]
# - life graphic
# - wrong guess reveals a letter from the answer.

class CricGuesserWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cric Guesser")
        self.geometry("620x430")
        self.resizable(False, False)

        self.life_art = {
            6: ("   ",
                "   ",
                "   "),
            5: (" 👽 ",
                "   ",
                "   "),
            4: (" 👽 ",
                " | ",
                "   "),
            3: (" 👽 ",
                "/| ",
                "   "),
            2: (" 👽 ",
                "/|\\",
                "   "),
            1: (" 👽 ",
                "/|\\",
                "/  "),
            0: (" 👽 ",
                "/|\\",
                "/ \\")
        }

        self.answer = ""
        self.hint = []
        self.wrong_guesses = 0
        self.guessed_letters = set()
        self.game_running = False

        title = tk.Label(self, text="WELCOME TO GUESS THE CRICKETER 🏏",
                         font=("Arial", 16, "bold"))
        title.pack(pady=10)

        rules = tk.Label(
            self,
            text=(
                "RULES:\n"
                "You will have 6 chances to guess the correct name.\n"
                "Your life will be displayed by the alien graphic."
            ),
            font=("Arial", 10),
            justify="center"
        )
        rules.pack(pady=5)

        # Selection frame for role/country (replicates a, b choice)
        select_frame = tk.LabelFrame(self, text="Select role and country", padx=10, pady=10)
        select_frame.pack(pady=10, fill="x", padx=20)

        tk.Label(select_frame, text="Role:").grid(row=0, column=0, sticky="w")
        tk.Label(select_frame, text="Country:").grid(row=0, column=2, sticky="w")

        self.role_var = tk.StringVar(value="1")   # default Batsmen
        self.country_var = tk.StringVar(value="1")  # default India

        role_map = [
            ("Batsmen", "1"),
            ("All Rounders", "2"),
            ("Bowlers", "3"),
            ("Women", "4"),
        ]
        country_map = [
            ("India", "1"),
            ("Australia", "2"),
            ("England", "3"),
            ("New Zealand", "4"),
            ("South Africa", "5"),
            ("West Indies", "6"),
        ]

        role_menu = tk.OptionMenu(select_frame, self.role_var, *[r[1] for r in role_map])
        country_menu = tk.OptionMenu(select_frame, self.country_var, *[c[1] for c in country_map])

        # To make it clearer, also show labels for what numbers mean
        tk.Label(select_frame, text="1:Batsmen  2:All Rounders  3:Bowlers  4:Women")\
            .grid(row=1, column=0, columnspan=3, sticky="w", pady=(4, 0))
        tk.Label(select_frame, text="1:India  2:Aus  3:Eng  4:NZ  5:SA  6:WI")\
            .grid(row=2, column=0, columnspan=3, sticky="w")

        role_menu.grid(row=0, column=1, padx=5)
        country_menu.grid(row=0, column=3, padx=5)

        start_btn = tk.Button(select_frame, text="Start Game", command=self.start_game)
        start_btn.grid(row=0, column=4, padx=10)

        # Game area
        game_frame = tk.Frame(self)
        game_frame.pack(pady=10)

        self.life_label = tk.Label(game_frame, text="", font=("Courier", 14))
        self.life_label.grid(row=0, column=0, rowspan=3, padx=20)

        self.word_label = tk.Label(game_frame, text="", font=("Arial", 16))
        self.word_label.grid(row=0, column=1, padx=10, pady=5)

        self.status_label = tk.Label(game_frame, text="", font=("Arial", 10))
        self.status_label.grid(row=1, column=1, padx=10, pady=5)

        guess_frame = tk.Frame(self)
        guess_frame.pack(pady=10)

        tk.Label(guess_frame, text="Enter a letter: ").grid(row=0, column=0)
        self.guess_entry = tk.Entry(guess_frame, width=5)
        self.guess_entry.grid(row=0, column=1, padx=5)

        guess_btn = tk.Button(guess_frame, text="Guess", command=self.make_guess)
        guess_btn.grid(row=0, column=2, padx=5)

        self.guessed_label = tk.Label(self, text="Guessed letters: ", font=("Arial", 10))
        self.guessed_label.pack(pady=5)

    def start_game(self):
        # Build key like original code: c = a+b
        a = self.role_var.get()
        b = self.country_var.get()
        c = a + b

        valid_keys = [
            "11", "21", "31", "12", "22", "32",
            "13", "23", "33", "14", "24", "34",
            "15", "25", "35", "16", "26", "36",
            "41", "42", "43", "44", "45", "46"
        ]

        if c not in valid_keys:
            messagebox.showerror("Invalid input",
                                 "Invalid combination of role and country (like original game).")
            return

        words = ref.cric[c]

        # Set up the guessing game like in original
        self.answer = random.choice(words).lower()
        self.hint = ["_"] * len(self.answer)

        # reveal spaces
        for i in range(len(self.answer)):
            if self.answer[i] == " ":
                self.hint[i] = " "

        # reveal all occurrences of the first letter
        h = self.answer[0]
        for i in range(len(self.answer)):
            if self.answer[i] == h:
                self.hint[i] = h

        self.wrong_guesses = 0
        self.guessed_letters = set()
        self.game_running = True

        self.update_display()

    def update_display(self):
        # update life drawing
        wg = self.wrong_guesses
        if wg < 0:
            wg = 0
        if wg > 6:
            wg = 6
        lines = self.life_art[wg]
        self.life_label.config(text="\n".join(lines))

        # update word hint and guessed letters
        self.word_label.config(text=" ".join(self.hint))
        self.guessed_label.config(text=f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")
        self.status_label.config(text="")

    def make_guess(self):
        if not self.game_running:
            self.status_label.config(text="Click 'Start Game' to begin.")
            return

        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.status_label.config(text="Invalid input (enter a single letter).")
            return

        if guess in self.guessed_letters:
            self.status_label.config(text=f"'{guess}' is already guessed.")
            return

        self.guessed_letters.add(guess)

        if guess in self.answer:
            # reveal all occurrences
            for i in range(len(self.answer)):
                if self.answer[i] == guess:
                    self.hint[i] = guess
        else:
            # original logic: reveal a letter at index wrong_guesses, then increment
            if self.wrong_guesses < len(self.answer):
                self.hint[self.wrong_guesses] = self.answer[self.wrong_guesses]
            self.wrong_guesses += 1

        # check win/lose like original
        if "_" not in self.hint:
            # win
            self.update_display()
            messagebox.showinfo("YOU WIN!", f"The cricketer was:\n{self.answer}")
            self.game_running = False
        elif self.wrong_guesses >= 6:
            # lose
            self.update_display()
            messagebox.showinfo("YOU LOSE!", f"The cricketer was:\n{self.answer}")
            self.game_running = False
        else:
            self.update_display()


# ========================= RUN APP ========================= #

if __name__ == "__main__":
    app = GamingArcade()
    app.mainloop()
