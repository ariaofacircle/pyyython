# rock paper scissors girlie

import random
choices = ['rock', 'paper', 'scissor']

while True:
    compchoice = random.choice(choices)
    userchoice = input("\nRock, Paper or Scissor(q to quit): ").strip().lower()
    if userchoice == 'q':
        print("Thank you for playing!")
        break
    elif userchoice not in choices:
        print("Invalid input")  
    else:
        print(f"Computer choice: {compchoice}")
        if userchoice == compchoice:
            print("Tie!")
        elif userchoice == 'rock':
            print("You win" if compchoice == 'scissor' else "You lose")
        elif userchoice == 'paper':
            print("You win" if compchoice == 'rock' else "You lose")
        elif userchoice == 'scissor':
            print("You win" if compchoice == 'paper' else "You lose")
