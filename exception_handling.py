a = int(input("Enter number: "))
try:
    b = 10 / a
except ArithmeticError:  # handle error
    print("Arithmetic Error occur")
else:  # if error not occur
    print(b)
finally:
    print("Finally block excuted")
