# Following is an algorithm to classify numbers as a Single Digite, Double Digite or Big.
num=int(input("Enter the number- "))
if(num>=0 and num<=9):
    print(f"{num} is Single digit")
elif(num>9 and num<=99):
    print(f"{num} is Double digit")
else:
    print(f"{num} is Big")
