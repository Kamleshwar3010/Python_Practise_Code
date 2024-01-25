print("Enter First Number")
num1=int(input())
print("Enter Second Number")
num2=int(input())
print("Enter Third Number")
num3=int(input())

if num1>num2 and  num1>num3:
    print("First Number is Largest")
elif num2>num3:
    print("Second Number is Largest")
else:
    print("Third Number is Largest")
