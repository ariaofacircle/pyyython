# movie food

menu = {"Pizza":3.00,
        "Popcorn":6.00,
        "Fries":2.50,
        "Coke": 3.00}

cart = []
total = 0

print("Menu".center(15))
for food, price in menu.items():
    print(f"{food}", end="")
    print("-"*(15-len(food)), end="")
    print(f"{price}")

while True:
    order = input("\nWhat food would you like to buy: ")
    if order == "q":
        break
    elif menu.get(order) is None:
        print("That food does not exist here. Try again")
    else:
        print("Menu item succesfully added to cart")
        cart.append(order)

print()
print("CHECKOUT".center(15))
for food in cart:
    total += menu.get(food)
    print(f"{food}", end="")
    print("-"*(15-len(food)), end="")
    print(f"{menu.get(food)}")

print(f"\nTotal:---------{total}")
