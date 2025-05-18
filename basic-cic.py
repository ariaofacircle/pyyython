# compound interest calculator
# all user defined kay kapoy

while True:
    principal = float(input("Principle Amount: $"))
    if 100 <= principal < 10000000000:
        break
    else:
        print("Amount not allowed ( either too big or too little )") # tamad i justify uy, gusto ko pala greater than 100 :p

while True:
    interest = float(input("Interest Rate: "))
    if 0 <= interest:
        break
    else:
        print("Negative values are not allowed") # nyeah

while True:
    time = float(input("Time Elapsed ( in years ): "))
    if 0 < time:
        break
    else:
        print("Negative years does not exist :p") # unless time traveler ka, which not really parin actually ...

amount = principal * pow( ( 1+( interest/100 ) ),time ) # boom, favorite part fr

print()
print("Summary of Account".center(50))
print(f"Principal Amount: ${principal}".center(50))
print(f"Interest Rate: {interest} %".center(50))
print(f"Years Elapsed: {time} years".center(50))
print(f"The total compounded amount is: ${amount:,.2f}".center(50))
