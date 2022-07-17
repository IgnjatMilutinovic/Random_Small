from random import randint
def ColdWorld():
    Player = input()
    AI = randint(1,3)

    if Player == 'Rock':
        if AI == 1:
            print('Player selects Rock, AI selects Rock ')
            print('Its a Draw')
        if AI == 2:
            print('Player selects Rock, AI selects Paper')
            print('AI Won')
        if AI == 3:
            print('Player selects Rock, AI selects Scissors')
            print('Player Won')

    if Player == 'Paper':
        if AI == 1:
            print('Player selects Paper, AI selects Rock ')
            print('Player Won')
        if AI == 2:
            print('Player selects Paper, AI selects Paper')
            print('Its a Draw')
        if AI == 3:
            print('Player selects Paper, AI selects Scissors')
            print('AI Won')

    if Player == 'Scissors':
        if AI == 1:
            print('Player selects Scissors, AI selects Rock ')
            print('AI Won')
        if AI == 2:
            print('Player selects Scissors, AI selects Paper')
            print('Player Won')
        if AI == 3:
            print('Player selects Scissors, AI selects Scissors')
            print('Its a Draw')
    print("Game Ends")
ColdWorld()
input("Press ENTER to exit")




