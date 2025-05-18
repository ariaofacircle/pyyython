# triangle kasi memorable to masyado when I was still learning C++

rows = int(input("Row #: "))
symbol = input("Symbol: ")

# inverted right triangle ( left aligned )
for x in range(rows, 0, -1):
    print(symbol*x)

print()

# non - inverted right triangle ( right aligned )
for x in range(1, rows+1):
    print(symbol*x)

print()

# inverted right triangle ( right aligned )
for x in range(rows, 0, -1):
    print(" "*(rows-x), end="")
    print(symbol*x)

print()

# non-inverted right triangle ( right aligned )
for x in range(1, rows+1):
    print(" "*(rows-x), end="")
    print(symbol*x)

print()

# inverted triangle 
for x in range(rows, 0, -2):
    print(" "*int((rows-x)/2), end="")
    print(symbol*x, end="")
    print(" "*int((rows-x)/2))

print()

# triangle
for x in range(1, rows+1, 2):
    print(" "*int((rows-x)/2), end="") # lollll, brute force kay kapoy maghimo variable
    print(symbol*x, end="")
    print(" "*int((rows-x)/2))
