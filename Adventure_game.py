while True:
    print('Welcome to our spooky adventure game!!\n\nYou are going to your home in a dark night and your car had some problem in a lonely road.\nWhile you were analysing the situation another car came and stopped by to check on you.\nHe was an old man probabily in his 60s.\nHe offered you a lift and you have TWO choices :\n\nACCEPT it or REJECT it\n')

    choice1 = input('Enter yes or no for the answer :').lower()

    if choice1 == 'yes':
        print("He was the trinity killer and he killed you 💀 game over!!")

    elif choice1 == 'no':
        print("You said yes and now regretting your decision")
        
        print('You came to a decision to walk to the nearest gas station, it was 15 min away via walking\n\nwalking.....................\nYou saw something like a bear but you are not sure\n\nYou have two thoughts now:\n\n1)run faster silently\n2)walk in a usual speed ignoring the danger')
        
        choice2 = int(input('Enter your choice\n\n1 -->Run\n2 -->ignore the danger and continue... :'))

        if choice2 == 1:
            print("Running..... huh huh huh... You saw the gas station")

        elif choice2 == 2:
            print("walking..... oops!! You heared bears voice and started running ..... You survived and saw the gas station")

        print('You want something to drink and eat now after the bear event.\nYou saw a diet coke and a redbull\n')

        choice3 = int(input('1 -->diet coke\n2 -->redbull\nPick your choice:\n'))

        print("You were browsing through the shop and thinking what to do next.\nBut then you saw the same old man again , Looks like he is offereing you a ride again\n\nWould you like to take the ride??:")

        ride_choice = input("Enter yes to take the ride\nEnter no to book a cab\n\nEnter your choice: ").lower()

        if ride_choice == 'yes':
            print("He was the trinity killer and he killed you 💀 game over!!")

        elif ride_choice == 'no':
            print("Sorry I booked a cab it is gonna arrive soon")

        print("While you were checking out the shopkeeper tells you to stay safe as a serial killer is around hunting lonely people and told a story which resembles with the story of him and the old man tonight\n\nYoy have two options: \nTo call the cops and tell the whole story\nThink of it just as a coinsidence and go home via your cab\n")

        choice4 = int(input("\n1 --> Call the cops\n\n2 --> Ignore and leave\nEnter your choice: "))

        if choice4 == 1 or choice4 == 2:
            print("*🎊Woops you reached home safely after hell of a night 🎊*")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break







  # he meets trinity again
    # offer of ride yes or no
    # he will call a cab
    # shopkeeper while checking out tells the story of trinity killer matching his story he now he knows that man was the trinity killer but cant prove it
    # Goes home safely 
    # end
