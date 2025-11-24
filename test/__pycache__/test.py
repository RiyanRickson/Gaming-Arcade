import wx
import random
import ref  # uses your ref.cric dictionary


# ================== GAME LOGIC (NO input()/print() HERE) ==================

def play_rock_paper_scissors(player_choice: str) -> str:
    player_choice = player_choice.lower()
    options = ("rock", "paper", "scissors")

    if player_choice not in options:
        return "Invalid choice."

    computer = random.choice(options)

    lines = []
    lines.append("=== Rock-Paper-Scissors ===")
    lines.append(f"Player choice: {player_choice}")
    lines.append(f"Computer choice: {computer}")

    if player_choice == computer:
        lines.append("It's a tie!")
    elif player_choice == "rock" and computer == "scissors":
        lines.append("You win!")
    elif player_choice == "paper" and computer == "rock":
        lines.append("You win!")
    elif player_choice == "scissors" and computer == "paper":
        lines.append("You win!")
    else:
        lines.append("You lose!")

    return "\n".join(lines)


dice_design = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"
    ),
}


def roll_dice(num_dice: int) -> str:
    if num_dice <= 0:
        return "Number of dice must be at least 1."

    dice = []
    total = 0
    for _ in range(num_dice):
        value = random.randint(1, 6)
        dice.append(value)
        total += value

    lines = []
    lines.append(f"=== Dice Roll ({num_dice} dice) ===")

    for i, value in enumerate(dice, start=1):
        lines.append(f"Die {i}:")
        for line in dice_design[value]:
            lines.append(line)
        lines.append("")  # blank line between dice

    lines.append(f"Total: {total}")
    return "\n".join(lines)


def play_number_guess(lower: int, upper: int, guess: int) -> str:
    if upper < lower + 2:
        return f"Invalid limits: upper must be at least {lower + 2}."

    if not (lower <= guess <= upper):
        return f"Guess {guess} is out of range [{lower}, {upper}]."

    ans = random.randint(lower, upper)

    lines = []
    lines.append("=== Guess the Number ===")
    lines.append(f"Range: {lower} to {upper}")
    lines.append(f"Your guess: {guess}")
    lines.append(f"Answer: {ans}")

    if guess == ans:
        lines.append("You win!")
    else:
        lines.append("You lost!")

    return "\n".join(lines)


# Life art for cricketer game
life_art = {
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
        "/ \\"),
}


# ================== WX GUI ==================

class ArcadeFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(ArcadeFrame, self).__init__(*args, **kwargs)

        panel = wx.Panel(self)

        title = wx.StaticText(panel, label="🎮 Gaming Arcade (wxPython)")
        font = title.GetFont()
        font.PointSize += 4
        font = font.Bold()
        title.SetFont(font)

        self.output = wx.TextCtrl(
            panel,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2,
            size=(650, 420)
        )

        # Buttons for each game
        self.btn_rps = wx.Button(panel, label="Rock-Paper-Scissors")
        self.btn_dice = wx.Button(panel, label="Dice Roll")
        self.btn_guess = wx.Button(panel, label="Guess the Number")
        self.btn_adventure = wx.Button(panel, label="Adventure Game")
        self.btn_cricket = wx.Button(panel, label="Guess the Cricketer")

        # Layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(title, 0, wx.ALL | wx.ALIGN_CENTER, 10)
        main_sizer.Add(self.output, 1, wx.EXPAND | wx.ALL, 5)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(self.btn_rps, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_dice, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_guess, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_adventure, 0, wx.ALL, 5)
        btn_sizer.Add(self.btn_cricket, 0, wx.ALL, 5)

        main_sizer.Add(btn_sizer, 0, wx.ALIGN_CENTER)

        panel.SetSizer(main_sizer)

        # Bind button events
        self.btn_rps.Bind(wx.EVT_BUTTON, self.on_rps)
        self.btn_dice.Bind(wx.EVT_BUTTON, self.on_dice)
        self.btn_guess.Bind(wx.EVT_BUTTON, self.on_guess)
        self.btn_adventure.Bind(wx.EVT_BUTTON, self.on_adventure)
        self.btn_cricket.Bind(wx.EVT_BUTTON, self.on_cricket)

        self.print_banner()

    def append_output(self, text: str):
        if self.output.GetValue():
            self.output.AppendText("\n\n")
        self.output.AppendText(text)

    def print_banner(self):
        banner = (
            "👾      🎊    WELCOME TO THE GAMING-ARCADE    🎊   🐇\n"
            "   ⚔️        ✂️             🎩            🎲          \n"
        )
        self.append_output(banner)

    # ---------- Button Handlers ----------

    def on_rps(self, event):
        choices = ["rock", "paper", "scissors"]
        dlg = wx.SingleChoiceDialog(
            self,
            "Choose your move:",
            "Rock-Paper-Scissors",
            choices
        )
        if dlg.ShowModal() == wx.ID_OK:
            choice = dlg.GetStringSelection()
            result = play_rock_paper_scissors(choice)
            self.append_output(result)
        dlg.Destroy()

    def on_dice(self, event):
        dlg = wx.TextEntryDialog(
            self,
            "How many dice?",
            "Dice Roll",
            "1"
        )
        if dlg.ShowModal() == wx.ID_OK:
            text = dlg.GetValue()
            try:
                num = int(text)
                result = roll_dice(num)
            except ValueError:
                result = "Invalid number of dice."
            self.append_output(result)
        dlg.Destroy()

    def on_guess(self, event):
        # lower limit
        dlg_l = wx.TextEntryDialog(
            self,
            "Enter the lower limit:",
            "Guess the Number",
            "1"
        )
        if dlg_l.ShowModal() != wx.ID_OK:
            dlg_l.Destroy()
            return
        try:
            lower = int(dlg_l.GetValue())
        except ValueError:
            self.append_output("Invalid lower limit.")
            dlg_l.Destroy()
            return
        dlg_l.Destroy()

        # upper limit
        dlg_u = wx.TextEntryDialog(
            self,
            f"Enter the upper limit (>= {lower + 2}):",
            "Guess the Number",
            str(lower + 5)
        )
        if dlg_u.ShowModal() != wx.ID_OK:
            dlg_u.Destroy()
            return
        try:
            upper = int(dlg_u.GetValue())
        except ValueError:
            self.append_output("Invalid upper limit.")
            dlg_u.Destroy()
            return
        dlg_u.Destroy()

        # user guess
        dlg_g = wx.TextEntryDialog(
            self,
            f"Select a number between {lower} and {upper}:",
            "Guess the Number",
            str(lower)
        )
        if dlg_g.ShowModal() != wx.ID_OK:
            dlg_g.Destroy()
            return
        try:
            guess = int(dlg_g.GetValue())
        except ValueError:
            self.append_output("Invalid guess (not a number).")
            dlg_g.Destroy()
            return
        dlg_g.Destroy()

        result = play_number_guess(lower, upper, guess)
        self.append_output(result)

    def on_adventure(self, event):
        # You can later import Adventure_game and build a GUI interface for it
        self.append_output("Adventure Game (GUI version) not implemented yet.")

    def on_cricket(self, event):
        # 1) Choose role
        roles = ["Batsmen", "All Rounders", "Bowlers", "Women"]
        dlg_role = wx.SingleChoiceDialog(
            self,
            "From what role of players would you like to guess?",
            "Guess the Cricketer - Role",
            roles
        )
        if dlg_role.ShowModal() != wx.ID_OK:
            dlg_role.Destroy()
            return
        role_index = dlg_role.GetSelection()   # 0..3
        dlg_role.Destroy()

        # 2) Choose country
        countries = ["India", "Australia", "England", "New Zealand", "South Africa", "West Indies"]
        dlg_country = wx.SingleChoiceDialog(
            self,
            "From which country?",
            "Guess the Cricketer - Country",
            countries
        )
        if dlg_country.ShowModal() != wx.ID_OK:
            dlg_country.Destroy()
            return
        country_index = dlg_country.GetSelection()  # 0..5
        dlg_country.Destroy()

        # Build key like your original code: a+b with "1","2","3","4" and "1".. "6"
        role_code = str(role_index + 1)
        country_code = str(country_index + 1)
        key = role_code + country_code

        if key not in ref.cric:
            self.append_output("Invalid role/country combination in ref.cric.")
            return

        words = ref.cric[key]
        answer = random.choice(words).lower()

        # Prepare hint list
        hint = ["_"] * len(answer)
        for i, ch in enumerate(answer):
            if ch == " ":
                hint[i] = " "

        # reveal first letter everywhere it appears
        first_letter = answer[0]
        for i, ch in enumerate(answer):
            if ch == first_letter:
                hint[i] = first_letter

        wrong_guesses = 0
        guessed_letters = set()
        max_wrong = 6
        is_running = True

        # Header
        header = (
            "WELCOME TO GUESS THE CRICKETER 🏏\n"
            "RULES:\n"
            "- You have 6 chances to guess the correct name.\n"
            "- Your life will be displayed by the graphic.\n"
            f"- Role: {roles[role_index]}, Country: {countries[country_index]}\n"
        )
        self.append_output(header)

        # Game loop using dialogs
        while is_running:
            # Build life + hint string
            lines = []
            lines.append("LIFE:")
            life_state = life_art[wrong_guesses]   # use wrong_guesses directly
            for line in life_state:
                lines.append(line)

            lines.append("")
            lines.append("Current Hint:")
            lines.append(" ".join(hint))
            lines.append("")
            lines.append(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
            lines.append(
                f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}"
            )

            self.append_output("\n".join(lines))

            # Ask for a letter
            dlg_guess = wx.TextEntryDialog(
                self,
                "Enter a letter (a-z):",
                "Guess the Cricketer",
                ""
            )
            if dlg_guess.ShowModal() != wx.ID_OK:
                dlg_guess.Destroy()
                self.append_output("Game cancelled.")
                return
            guess = dlg_guess.GetValue().strip().lower()
            dlg_guess.Destroy()

            # Validate guess
            if len(guess) != 1 or not guess.isalpha():
                self.append_output("Invalid input. Please enter a single letter.")
                continue

            if guess in guessed_letters:
                self.append_output(f"'{guess}' is already guessed.")
                continue

            guessed_letters.add(guess)

            if guess in answer:
                # reveal all positions
                for i, ch in enumerate(answer):
                    if ch == guess:
                        hint[i] = guess
                self.append_output(f"Good guess! '{guess}' is in the name.")
            else:
                # reveal one correct letter at index = wrong_guesses (like your code)
                if wrong_guesses < len(answer):
                    hint[wrong_guesses] = answer[wrong_guesses]
                wrong_guesses += 1
                self.append_output(f"Sorry, '{guess}' is not in the name.")

            # Check win/lose
            if "_" not in hint:
                final_lines = []
                final_lines.append("FINAL LIFE STATE:")
                life_state = life_art[wrong_guesses]
                for line in life_state:
                    final_lines.append(line)






                final_lines.append("")
                final_lines.append("ANSWER:")
                final_lines.append(" ".join(answer))
                final_lines.append("YOU WIN! 🎉")

                self.append_output("\n".join(final_lines))
                is_running = False

            elif wrong_guesses >= max_wrong:
                final_lines = []
                final_lines.append("FINAL LIFE STATE:")
                life_state = life_art[wrong_guesses]   # at this point wrong_guesses == 6
                for line in life_state:
                    final_lines.append(line)

                final_lines.append("")
                final_lines.append("ANSWER:")
                final_lines.append(" ".join(answer))
                final_lines.append("YOU LOSE! 😢")

                self.append_output("\n".join(final_lines))
                is_running = False


class ArcadeApp(wx.App):
    def OnInit(self):
        frame = ArcadeFrame(None, title="Gaming Arcade (wxPython)", size=(900, 600))
        frame.Show()
        return True


if __name__ == "__main__":
    app = ArcadeApp(False)
    app.MainLoop()

