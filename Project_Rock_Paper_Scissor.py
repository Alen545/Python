import random
userChoice = int(input('Type for 0 for Rock, 1 for Paper, 2 for Scissor:'))
if userChoice >= 2 or userChoice < 0:
    print('You Entered Wrong Value, You Lose the Game!!!')
else:
    computerChoice = random.randint(0,2)
    print(computerChoice)
    if userChoice == computerChoice:
        print('Game is Draw')
    elif userChoice == 0 and computerChoice == 2:
        print('You Win')
    elif userChoice == 2 and computerChoice == 0:
        print('You Lose')
    elif userChoice > computerChoice:
        print('You win')
    elif computerChoice > userChoice:
        print('You Lose')

