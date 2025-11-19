import random
#● ┌ ─ ┐ │ └ ┘
dice_design={
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"
       ),
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│       ● │",
       "└─────────┘"
       ),
    3:("┌─────────┐",
       "│  ●      │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘"
       ),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"
       ),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"
       ),
    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘"
       )
    
}
def dice_game():
    dice=[]
    total=0
    num_dice=int(input("How many dice?"))
    for i in range(num_dice):
        dice.append(random.randint(1,6))
    for k in range(num_dice):
        for l in dice_design.get(dice[k]):
            print(l)
    for j in dice:
        total+=j
    print(f'Total:{total}')


