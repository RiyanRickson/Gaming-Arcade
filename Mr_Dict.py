import random
import ref

life_art = {6: ("   ",
                                   "   ",
                                   "   "),
                             5: (" o ",
                                   "   ",
                                   "   "),
                             4: (" o ",
                                   " | ",
                                   "   "),
                             3: (" o ",
                                   "/| ",
                                   "   "),
                             2: (" o ",
                                  "/|\\",
                                   "   "),
                              1: (" o ",
                                   "/|\\",
                                   "/  "),
                              0: (" o ",
                                   "/|\\",
                                   "/ \\")}



def display_man(wrong_guesses):
    print("**********")
    print("LIFE=")
    for line in life_art[wrong_guesses]:
        print(line)
    print("**********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    print("from what set of words would you like to guess?","1:Indian foods","2:Fruits","3:Indian states and ut","4:Cricketers" ,sep="\n")
    gset=int(input("your choice:"))
    match gset:
        case 1:
            words=ref.indian_foods
        case 2:
            words=ref.fruits
        case 3:
            words=ref.indian_states_and_ut
        case 4:
            words=ref.indian_cricketers
        case _:
            print("Invalid input")
            exit
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(life_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()