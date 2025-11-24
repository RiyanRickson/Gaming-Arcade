import tkinter as tk
from tkinter import messagebox
import random
import ref



class GamingArcade(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gaming Arcade")

        self.attributes("-fullscreen", True)
        self.is_fullscreen = True
        self.bind("<Escape>", self.exit_fullscreen)

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

        toggle_full_btn = tk.Button(self, text="Toggle Fullscreen", width=20,
                                    command=self.toggle_fullscreen)
        toggle_full_btn.pack(pady=10)

        quit_btn = tk.Button(self, text="Exit", width=10, command=self.destroy)
        quit_btn.pack(pady=10)

    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        self.attributes("-fullscreen", self.is_fullscreen)

    def exit_fullscreen(self, event):
        self.is_fullscreen = False
        self.attributes("-fullscreen", False)


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


class NumberGuessWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Number Guessing Game")
        self.geometry("420x320")
        self.resizable(False, False)

        title = tk.Label(self, text="Number Guessing Game", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        info = tk.Label(self, text="Enter lower limit, upper limit, and your guess.",
                        font=("Arial", 10), justify="center")
        info.pack(pady=5)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Lower limit (l):").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(form, text="Upper limit (u):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Label(form, text="Your guess:").grid(row=2, column=0, sticky="e", padx=5, pady=5)

        self.lower_entry = tk.Entry(form, width=10)
        self.upper_entry = tk.Entry(form, width=10)
        self.guess_entry = tk.Entry(form, width=10)

        self.lower_entry.grid(row=0, column=1, padx=5, pady=5)
        self.upper_entry.grid(row=1, column=1, padx=5, pady=5)
        self.guess_entry.grid(row=2, column=1, padx=5, pady=5)

        play_btn = tk.Button(self, text="Play", command=self.play_once)
        play_btn.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 11))
        self.result_label.pack(pady=10)

    def play_once(self):
        try:
            l = int(self.lower_entry.get())
            u = int(self.upper_entry.get())
        except ValueError:
            self.result_label.config(text="invalid limits")
            return

        usans_str = self.guess_entry.get()
        if not usans_str.isdigit():
            self.result_label.config(text="Invalid guess")
            return

        usans = int(usans_str)

        if l == u or l > u or u < l + 2:
            self.result_label.config(text="invalid limits")
            return
        if usans < l or usans > u:
            self.result_label.config(text=" guess out of range")
            return

        ans = random.randint(l, u)
        if usans == ans:
            self.result_label.config(text="You win!")
        else:
            self.result_label.config(text="You lost!")


DICE_DESIGN = {
    1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│  ●      │", "│         │", "│       ● │", "└─────────┘"),
    3: ("┌─────────┐", "│  ●      │", "│    ●    │", "│       ● │", "└─────────┘"),
    4: ("┌─────────┐", "│ ●     ● │", "│         │", "│ ●     ● │", "└─────────┘"),
    5: ("┌─────────┐", "│ ●     ● │", "│    ●    │", "│ ●     ● │", "└─────────┘"),
    6: ("┌─────────┐", "│ ●     ● │", "│ ●     ● │", "│ ●     ● │", "└─────────┘")
}


class DiceWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Dice Game")
        self.geometry("420x360")
        self.resizable(False, False)

        title = tk.Label(self, text="Dice Game", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="How many dice?").grid(row=0, column=0, padx=5, pady=5)
        self.num_entry = tk.Entry(input_frame, width=10)
        self.num_entry.grid(row=0, column=1, padx=5, pady=5)

        roll_btn = tk.Button(self, text="Roll", command=self.roll_dice)
        roll_btn.pack(pady=5)

        self.dice_label = tk.Label(self, text="", font=("Courier", 12), justify="left")
        self.dice_label.pack(pady=10)

        self.total_label = tk.Label(self, text="", font=("Arial", 11))
        self.total_label.pack(pady=5)

        self.status_label = tk.Label(self, text="", font=("Arial", 10))
        self.status_label.pack(pady=5)

    def roll_dice(self):
        try:
            num_dice = int(self.num_entry.get())
        except ValueError:
            self.status_label.config(text="Invalid number of dice")
            self.dice_label.config(text="")
            self.total_label.config(text="")
            return

        if num_dice <= 0:
            self.status_label.config(text="Number of dice should be positive")
            self.dice_label.config(text="")
            self.total_label.config(text="")
            return

        dice = [random.randint(1, 6) for _ in range(num_dice)]
        total = sum(dice)

        lines = []
        for value in dice:
            for line in DICE_DESIGN[value]:
                lines.append(line)
            lines.append("")

        self.dice_label.config(text="\n".join(lines))
        self.total_label.config(text=f"Total:{total}")
        self.status_label.config(text="")


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
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
        ]
        return any(self.board[a] == self.board[b] == self.board[c] == player for a, b, c in wins)

    def reset_board(self):
        self.board = [None] * 9
        for b in self.btns:
            b.config(text="")
        self.current_player = "X"
        self.info_label.config(text="Player X's turn")


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
                    "He offered you a lift and you have TWO choices :\n\n"
                    "ACCEPT it or REJECT it\n"
                )
            )
            self.choice1_btn.config(text="Accept the ride (yes)")
            self.choice2_btn.config(text="Reject the ride (no)")

        elif self.state == "death_trinity":
            self.text_label.config(
                text="He was the trinity killer and he killed you 💀 game over!!"
            )
            self.choice1_btn.config(text="Play again")
            self.choice2_btn.config(text="Close")

        elif self.state == "walk_bear_intro":
            self.text_label.config(
                text=(
                    "You said yes and now regretting your decision\n\n"
                    "You came to a decision to walk to the nearest gas station, it was 15 min away via walking\n\n"
                    "walking.....................\n"
                    "You saw something like a bear but you are not sure\n\n"
                    "You have two thoughts now:\n\n"
                    "1)run faster silently\n"
                    "2)walk in a usual speed ignoring the danger"
                )
            )
            self.choice1_btn.config(text="Run faster silently (1)")
            self.choice2_btn.config(text="Ignore and walk (2)")

        elif self.state == "after_run":
            self.text_label.config(
                text=(
                    "Running..... huh huh huh... You saw the gas station\n\n"
                    "You want something to drink and eat now after the bear event.\n"
                    "You saw a diet coke and a redbull\n"
                )
            )
            self.choice1_btn.config(text="diet coke (1)")
            self.choice2_btn.config(text="redbull (2)")

        elif self.state == "after_walk_ignore":
            self.text_label.config(
                text=(
                    "walking..... oops!! You heared bears voice and started running ..... "
                    "You survived and saw the gas station\n\n"
                    "You want something to drink and eat now after the bear event.\n"
                    "You saw a diet coke and a redbull\n"
                )
            )
            self.choice1_btn.config(text="diet coke (1)")
            self.choice2_btn.config(text="redbull (2)")

        elif self.state == "ride_offer_again":
            self.text_label.config(
                text=(
                    "You were browsing through the shop and thinking what to do next.\n"
                    "But then you saw the same old man again , Looks like he is offereing you a ride again\n\n"
                    "Would you like to take the ride??:"
                )
            )
            self.choice1_btn.config(text="Take the ride (yes)")
            self.choice2_btn.config(text="Book a cab (no)")

        elif self.state == "ride_no_cab":
            self.text_label.config(
                text=(
                    "Sorry I booked a cab it is gonna arrive soon\n\n"
                    "While you were checking out the shopkeeper tells you to stay safe as a serial killer is "
                    "around hunting lonely people and told a story which resembles with the story of him and "
                    "the old man tonight\n\n"
                    "Yoy have two options: \n"
                    "To call the cops and tell the whole story\n"
                    "Think of it just as a coinsidence and go home via your cab\n"
                )
            )
            self.choice1_btn.config(text="Call the cops (1)")
            self.choice2_btn.config(text="Ignore and leave (2)")

        elif self.state == "home_safe":
            self.text_label.config(
                text="*🎊Woops you reached home safely after hell of a night 🎊*"
            )
            self.choice1_btn.config(text="Play again")
            self.choice2_btn.config(text="Close")

    def on_choice1(self):
        if self.state == "choice1":
            self.state = "death_trinity"
        elif self.state == "death_trinity":
            self.state = "choice1"
        elif self.state == "walk_bear_intro":
            self.state = "after_run"
        elif self.state in ("after_run", "after_walk_ignore"):
            self.state = "ride_offer_again"
        elif self.state == "ride_offer_again":
            self.state = "death_trinity"
        elif self.state == "ride_no_cab":
            self.state = "home_safe"
        elif self.state == "home_safe":
            self.state = "choice1"
        self.update_scene()

    def on_choice2(self):
        if self.state == "choice1":
            self.state = "walk_bear_intro"
        elif self.state == "death_trinity":
            self.destroy()
            return
        elif self.state == "walk_bear_intro":
            self.state = "after_walk_ignore"
        elif self.state in ("after_run", "after_walk_ignore"):
            self.state = "ride_offer_again"
        elif self.state == "ride_offer_again":
            self.state = "ride_no_cab"
        elif self.state == "ride_no_cab":
            self.state = "home_safe"
        elif self.state == "home_safe":
            self.destroy()
            return
        self.update_scene()

    def restart(self):
        self.state = "choice1"
        self.update_scene()


class CricGuesserWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cric Guesser")
        self.geometry("620x430")
        self.resizable(False, False)

        self.life_art = {
            6: ("   ", "   ", "   "),
            5: (" 👽 ", "   ", "   "),
            4: (" 👽 ", " | ", "   "),
            3: (" 👽 ", "/| ", "   "),
            2: (" 👽 ", "/|\\", "   "),
            1: (" 👽 ", "/|\\", "/  "),
            0: (" 👽 ", "/|\\", "/ \\")
        }

        self.answer = ""
        self.hint = []
        self.wrong_guesses = 0
        self.guessed_letters = set()
        self.game_running = False

        title = tk.Label(self, text="WELCOME TO GUESS THE CRICKETER 🏏",
                         font=("Arial", 16, "bold"))
        title.pack(pady=10)

        rules = tk.Label(self,
                         text="You will have 6 chances to guess the correct name-\nYour life will be displayed by the graphic",
                         font=("Arial", 10), justify="center")
        rules.pack(pady=5)

        select_frame = tk.LabelFrame(self, text="Select role and country", padx=10, pady=10)
        select_frame.pack(pady=10, fill="x", padx=20)

        tk.Label(select_frame, text="Role:").grid(row=0, column=0, sticky="w")
        tk.Label(select_frame, text="Country:").grid(row=0, column=2, sticky="w")

        self.role_var = tk.StringVar(value="1")
        self.country_var = tk.StringVar(value="1")

        role_menu = tk.OptionMenu(select_frame, self.role_var, "1", "2", "3", "4")
        country_menu = tk.OptionMenu(select_frame, self.country_var, "1", "2", "3", "4", "5", "6")

        tk.Label(select_frame, text="1:Batsmen  2:All Rounders  3:Bowlers  4:Women")\
            .grid(row=1, column=0, columnspan=5, sticky="w", pady=(4, 0))
        tk.Label(select_frame, text="1:India  2:Australia  3:England  4:New Zealand  5:South Africa  6:West Indies")\
            .grid(row=2, column=0, columnspan=5, sticky="w")

        role_menu.grid(row=0, column=1, padx=5)
        country_menu.grid(row=0, column=3, padx=5)

        start_btn = tk.Button(select_frame, text="Start Game", command=self.start_game)
        start_btn.grid(row=0, column=4, padx=10)

        game_frame = tk.Frame(self)
        game_frame.pack(pady=10)

        self.life_label = tk.Label(game_frame, text="", font=("Courier", 14), justify="left")
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
        a = self.role_var.get()
        b = self.country_var.get()
        c = a + b

        valid_keys = [
            "11", "21", "31",
            "12", "22", "32",
            "13", "23", "33",
            "14", "24", "34",
            "15", "25", "35",
            "16", "26", "36",
            "41", "42", "43", "44", "45", "46"
        ]

        if c not in valid_keys:
            messagebox.showerror("Invalid input", "Invalid combination")
            self.game_running = False
            return
        else:
            words = ref.cric[c]

        self.answer = random.choice(words).lower()
        self.hint = ["_"] * len(self.answer)

        for i in range(len(self.answer)):
            if self.answer[i] == " ":
                self.hint[i] = " "

        h = self.answer[0]
        for i in range(len(self.answer)):
            if self.answer[i] == h:
                self.hint[i] = h

        self.wrong_guesses = 0
        self.guessed_letters = set()
        self.game_running = True

        self.update_display()

    def update_display(self):
        wg = self.wrong_guesses
        if wg in self.life_art:
            lines = self.life_art[wg]
        else:
            lines = ("   ", "   ", "   ")

        self.life_label.config(text="LIFE=\n" + "\n".join(lines))
        self.word_label.config(text=" ".join(self.hint))
        self.guessed_label.config(
            text="Guessed letters: " + (", ".join(sorted(self.guessed_letters)) if self.guessed_letters else "")
        )
        self.status_label.config(text="")

    def make_guess(self):
        if not self.game_running:
            self.status_label.config(text="Click 'Start Game' to begin.")
            return

        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.status_label.config(text="Invalid input")
            return

        if guess in self.guessed_letters:
            self.status_label.config(text=f"{guess} is already guessed")
            return

        self.guessed_letters.add(guess)

        if guess in self.answer:
            for i in range(len(self.answer)):
                if self.answer[i] == guess:
                    self.hint[i] = guess
        else:
            self.hint[self.wrong_guesses] = self.answer[self.wrong_guesses]
            self.wrong_guesses += 1

        if "_" not in self.hint:
            self.update_display()
            messagebox.showinfo("YOU WIN!", " ".join(self.answer))
            self.game_running = False
        elif self.wrong_guesses >= 6:
            self.update_display()
            messagebox.showinfo("YOU LOSE!", " ".join(self.answer))
            self.game_running = False
        else:
            self.update_display()


if __name__ == "__main__":
    app = GamingArcade()
    app.mainloop()
