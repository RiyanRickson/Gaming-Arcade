import random
import ref
def cric_game():
    print("WELCOME TO GUESS THE CRICKETER🏏","\nRULES:\n","You will have 6 chances to guess the correct name-","your life will be displayed by the graphic",sep="\n")

    life_art = {6: ("   ",
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
                                    "/ \\")}



    def display_man(wrong_guesses):
        print("\n**********\n")
        print("LIFE=")
        for line in life_art[wrong_guesses]:
            print(line)
        print("\n**********\n")

    def display_hint(hint):
        print(" ".join(hint))

    def display_answer(answer):
        print(" ".join(answer))

    def main():
        print("\nfrom what role of players would you like to guess?","1:Batsmen","2:All Rounders","3:Bowlers","4:Women" ,sep="\n")
        a=input("Choice:  ")
        print("From which country? ","1: India","2: Australia","3: England","4: New Zealand","5: South Africa","6: West Indies",sep="\n")
        b=input("Choice: ")
        c=a+b

        if c not in ["11","21","31","12","22","32","13","23","33","14","24","34","15","25","35","16","26","36","41","42","43","44","45","46"]:
            print("Invalid input")
            exit
        else:
            words=ref.cric[c]

        
    
        answer = random.choice(words).lower()
        hint = ["_"] * len(answer)
        for i in range(len(answer)):
            if answer[i]==" ":
                hint[i]=" "
        h=answer[0]
        for i in range(len(answer)):
            if answer[i]==h:
                hint[i]=h
                
        
        wrong_guesses = 0
        guessed_letters = set()
        is_running = True

        while is_running:
            display_man(wrong_guesses)
            display_hint(hint)
            guess= input("Enter a letter: ").lower()

            if len(guess) != 1 or  not guess.isalpha():
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
                hint[wrong_guesses]=answer[wrong_guesses]
                wrong_guesses += 1

            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(answer)
                print("YOU WIN!")
                is_running = False
            elif wrong_guesses >= 6:
                display_man(wrong_guesses)
                display_answer(answer)
                print("YOU LOSE!")
                is_running = False

    main()