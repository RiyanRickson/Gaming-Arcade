############################################################
print("👾      🎊    WELCOME TO THE GAMING-ARCADE    🎊   🐇 ")
print("   ⚔️        ✂️             🎩            🎲          ")

 #

##########################################################
#importing dice game
import Dice
import Rockps
import numguess
import Adventure_game

def main_page():   
    print("WELCOME!!", "1 --> ROCK-PAPER-SCISSORS", "2 --> DICE ROLL" ,"3 --> GUESS THE NUMBER??!!","4 --> Adventure_game" ,"ENTER YOUR CHOICE: ",sep="\n" )
    CHOOSE_THE_GAME_BUTTON=int(input())

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
    elif CHOOSE_THE_GAME_BUTTON==4:
        game_run=True
        while game_run:
            Adventure_game.adventur_game()
            if not input("Play again?(y/n): ").lower()=="y":
                break
        

    else:
        print("OOPS ENTERED WRONG CHOICE PLZ TRY AGAIN")
    
main_run=True
while main_run:
     main_page()
     if not input("Change game and play? (y/n): ").lower()=="y":
          break
