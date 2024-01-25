# Practise Question 13
num=int(input("Enter The Number To Get Factorial- "))
i=num-1
print(num,end="")
while(i>0):
    print(f" X {i}",end="")
    num*=i
    i=i-1
print(f" = {num}")
