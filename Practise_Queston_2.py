# two friend decide who gets the last slice of a cacke by flipping coin five times an input-1 means plyer one wins else player two wins

i = p1 = p2 = 0
while (i < 5):
    a = int(input("Enter The Number between 1 and 2 - "))
    if a == 1 or a == 2:
        if a == 1:
            p1 = p1+1
        elif a == 2:
            p2 = p2+1
    else:
        print("Invalid Value : Enter The Number between 1 and 2")
        continue
    i = i+1


if (p1 > p2):
    print("Player one win")
else:
    print("Player two win")
