import random
def numgame():
    l=int(input("Enter the lower limit:"))
    u=int(input(f"Enter the upper limit(greater than {l}+2):"))
    ans=random.randint(l,u)
    usans=input(f"select a number between{l}and{u} :")
    if usans.isdigit():
        usans=int(usans)
        if l==u or l>u or u<l+2:
            print("invalid limits")
            numgame()
        elif usans<l or usans>u:
            print(" guess out of range")
            numgame()
        else:
            if usans==ans:
                print("You win!")
            else:
                print("You lost!")
    else:
        print("Invalid guess")
