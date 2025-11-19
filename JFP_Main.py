############################################################
print("👾      🎊    WELCOME TO THE GAMING-ARCADE    🎊   🐇 ")
print("   ⚔️        ✂️             🎩            🎲          ")

 #

##########################################################
#importing dice game
import Dice
import Rockps
import numguess

    
CHOOSE_THE_GAME_BUTTON = int(input("WELCOME!!\n" "1 --> ROCK-PAPER-SCISSORS\n" "2 --> DICE ROLL\n" "3 --> GUESS THE NUMBER??!!\n\n" "ENTER YOUR CHOICE: " ))

if CHOOSE_THE_GAME_BUTTON == 1:
    game_run=True
    while game_run:
        Rockps.rockps_game()
        if not input("Play again?(y/n)").lower()=="y":
            break

elif CHOOSE_THE_GAME_BUTTON == 2:
    game_run=True
    while game_run:
            Dice.dice_game()
            if not input("Play again?(y/n)").lower()=="y":
                 break
        

elif CHOOSE_THE_GAME_BUTTON == 3:
      game_run=True
      while game_run:
            numguess.numgame()
            if not input("Play again?(y/n)").lower()=="y":
                break
    

else:
    print("OOPS ENTERED WRONG CHOICE PLZ TRY AGAIN")
    

