"""Write an algorithm that performs the following:
Ask a user to enter a number. If the number is between 5 and 15, write the word GREEN. If the number is between 15 and 25, write the word BLUE.
If the number is between 25 and 35, write the word ORANGE. If it is any other number, write that ALL COLOURS ARE BEAUTIFUL.
"""
num = int(input("Enter the numbe- "))
if num >= 5 and num <= 15:
    print("GREEN")
elif num > 15 and num <= 25:
    print("BLUE")
elif num > 25 and num <= 35:
    print("ORANGE")
else:
    print("ALL COLOURS ARE BEAUTIFU")
