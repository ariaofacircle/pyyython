import time, random

while True:
    try:
        prodprime = int(input("Input a number ( product of 2 primes ) : "))

        g = int(input(f"Input a number with no shared factors (2 ≤ g < {prodprime}): "))

        # sad kaayo pero in the future ka nalang girl. once mas marunong na ako

        # print("\n   >>> Randomly generating a number : ", end="")

        # for x in range(10):
            # g = random.randint(2, prodprime-1)
            # print(f"\r  >>> Randomly generating a number: {g} ", end="", flush=True)
            # time.sleep(0.2)

        print("\n  >>> Finding smallest r such that g^r ≡ 1 mod N...")
        print("     ", end="")
        power = 1
        while True:
            remainder = pow(g, power) % prodprime

            if remainder == 1:
                break
            else:
                power += 1

        if power % 2 != 0:
            print("\nThis r won't work given the algorithm design. Please try again :((")
            continue
        else:
            top = pow(g, power//2) + 1
            bottom = prodprime
            # Euclid's algorithm
            while True:
                value = top % bottom
                top = bottom
                bottom = value

                if (value == 0):
                    break
            if (top == prodprime):
                print("\nThis r won't work given the algorithm design. Please try again :((\n" \
                f"It would lead to {prodprime} and 1 (lol)")
                continue
            else:
                f1 = top
                f2 = int(prodprime / f1)
                print(f"Factors of {prodprime}: {f1} and {f2}")
                break

    except ValueError:
        print("Numbers please :D")
        continue
