import random

dice_art = {
    1: ("""        ┌─────────┐
        │         │
        │    ●    │
        │         │
        └─────────┘"""),
    2: ("""        ┌─────────┐
        │  ●      │
        │         │
        │      ●  │
        └─────────┘"""),
    3: ("""        ┌─────────┐
        │  ●      │
        │    ●    │
        │      ●  │
        └─────────┘"""),
    4: ("""        ┌─────────┐
        │  ●   ●  │
        │         │
        │  ●   ●  │
        └─────────┘"""),
    5: ("""        ┌─────────┐
        │  ●   ●  │
        │    ●    │
        │  ●   ●  │
        └─────────┘"""),
    6: ("""        ┌─────────┐
        │  ●   ●  │
        │  ●   ●  │
        │  ●   ●  │
        └─────────┘""")
}

while True:
    total = 0
    try:
        dicenum = int(input("How many dices do you have (2009 to quit): "))

        if dicenum == 2009: # like a password of sorts
            break

        for dice in range(dicenum):
            roll = random.randint(1, 6)
            for num, art in dice_art.items():
                if num == roll:
                    print(art)
                    total += num
        print(f"{total}".center(27))

    except ValueError:
        print("Please input a number")
