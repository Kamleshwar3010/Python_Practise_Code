print("Programme to check Palindrome string")
val=input("Enter the value-\t")
if val[::-1] == val:
    print(val," is palindrome")
else:
    print(val,"is not a palindrome string")
