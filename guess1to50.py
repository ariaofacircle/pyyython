# random number guesser
import random

compchoice = random.randint(0, 50)
while True:
    try:
        userchoice = int(input("\nGuess the number (0-50): "))

        if compchoice == userchoice:
            print("Correct!")
            break
        elif compchoice > userchoice:
            print(f"{userchoice} is too little")
        else:
            print(f"{userchoice} is too high")
    except ValueError:
        print("Please input a number")

    
