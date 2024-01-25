""". A teacher asked his student Can you find two consecutive cube numbers in integers whose difference shall be a square number? Thus, the cube of 3 is 27, and the cube of 2 is 8, but the difference is that 19, is not here a square number. What is the smallest possible case?"""
import math
req = root = i = 1
# loop is run infinite time until condition is met
while (True):
    req = ((i+1)**3)-(i**3)  # check difference of i and i+1
    root = math.sqrt(req)  # find sq. root of req variable
    if root.is_integer():  # if root is perfect square (i.e is in integer not in float) then
        print(
            f"the cube of {i+1} is {(i+1)**3} and {i} is {i**3} and there differance is {req} which is square of {root:.0f}")
        break  # break the loop
    i += 1


# Fermat's theorem
for i in range(1, int(root)):
    for j in range(1, int(root)):
        if (((i**2)+(j**2)) == req):
            break

print(f"square of {i} is {i**2} and {j} is {j**2} whose sum is equal to {req}")


# import math
# req=root=i=1
# # loop is run infinite time until condition is met
# while(i< 10000):
#     req= ((i+1)**3)-(i**3) #check difference of i and i+1
#     root = math.sqrt(req) #find sq. root of req variable
#     if root.is_integer(): # if root is perfect square (i.e is in integer not in float) then
#         print(f"the cube of {i+1} is {(i+1)**3} and {i} is {i**3} and there differance is {req} which is square of {root:.0f}")
#         #Fermat's theorem
#         for m in range(1,int(root)):
#             for j in range(1,int(root)):
#                 if(((m**2)+(j**2))==req):
#                     break
#         print(f"square of {m} is {m**2} and {j} is {j**2} whose sum is equal to {req}")
#     i+=1
