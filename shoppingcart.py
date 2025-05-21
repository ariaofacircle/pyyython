print("SHOPPING CART SYSTEM".center(200), end="\n")

print(
        "\nWelcome dear customer to the shopping cart system !!\n" \
        "Please pick any of these operations to get you started: \n"
        "1. Add to cart\n" \
        "2. Remove from cart\n" \
        "3. Clear cart\n" \
        "4. View cart\n" \
        "5. Checkout\n" \
        "q: quit"
    )

products = []
prices = []
choice = ('1','2','3','4','5', 'q')
subtotal = 0


# required logic: input validation, prevent errors when empty, 

while True:

    userchoice = input("\nChoice: ")

    if userchoice not in choice:
        print("Invalid. Please input something else")
    
    # add to cart
    # hala kulang pa diay quantity ( later na ah )
    elif userchoice == '1':
        products.append(input("\nProduct: ").lower().strip())
        while True:
            try: 
                prices.append(int(input("Price: ")))
                print(f"Item added successfully to cart") # specification what item coming soon !!
                break
            except ValueError: # ehehehe
                print("Enter a valid number pls :))")

    # remove from cart
    elif userchoice == '2':
        if not products:
            print("Your cart is empty")
        else:
            removal = input("\nProducts: ").lower().strip()
            if removal not in products or not products:
                print("Invalid. You did not add this item to cart")
            else:
                index = products.index(removal)
                products.remove(removal)
                prices.remove(prices[index])
                print("Item successfully removed from cart")

    # clear cart
    elif userchoice == '3':
        if not products:
            print("Your cart is empty")
        else:
            products.clear()
            prices.clear()
            print("Cart successfully cleared")

    # view cart
    elif userchoice == '4':
        if not products and not prices:
            print("Your cart is empty")
        else:
            print(f"\nProducts in your cart: {products}")
            print(f"Their corresponding prices: {prices}")  # optimize later on na wala nang brackets by using for loops ( ginatamad ako rn )

    # checkout
    # alphabetical order coming soon !! ( pag di na ako ginatamad )
    elif userchoice == '5':
        if not products:
            print("Your cart is empty")
        else:
            print(" CHECKOUT RECEIPT ".center(50))            
            for item in range(0, len(products)):
                print(products[item], end="     ".center(50-len(products[item]))) # so proud of myself for figuring this out
                print(prices[item])
                subtotal += prices[item]
            print(f"\nTotal amount: {subtotal}")
            break

    elif userchoice == 'q':
        break
    


print("Thank you for using the shopping cart system! Come back again!")
