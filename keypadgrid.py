num = ((1, 2, 3),
       (4, 5, 6),
       (7, 8, 9),
       ("*", 0, "#"))

for value in num:
    for chara in value:
        print(chara, end=" ")
    print()
