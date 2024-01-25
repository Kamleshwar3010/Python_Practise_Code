''' Let us write a pseudocode and draw a flowchart where multiple conditions are checked to categorize a person as either child (<13), teenager (>=13 but <20) or adult (>=20), based on the age specified:'''
age = int(input("Enter Your Age- "))
if age <= 0:
    print("Enter Correct Age")
elif age > 0 and age < 13:
    print("Child")
elif age >= 13 and age < 20:
    print("teenager")
else:
    print("Adult")
