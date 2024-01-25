""" Write pseudocode that will perform the following:Read the marks of three subjects: Computer Science, Mathematics and Physics, out of 100 Calculate the aggregate marks Calculate the percentage of marks"""
total = 0
n = int(input("How many syubject you have- "))
for i in range(n):
    subject = str(input("Enter The Subject Name- "))
    Marks = int(input("Enter The Marks Obtain- "))
    if Marks > 100:
        print("please enter valid marks")
        Marks = int(input("Enter The Marks Obtain- "))
    else:
        total += Marks

print(f"Your Total Percentage  is {total/n}")
print(f"Aggregate Marks is {total/i+1}")
