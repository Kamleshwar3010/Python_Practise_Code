''' Question No. 1 (Practise set-3)'''
print("How many element you want in your list-\t", end="")
n = int(input())
list1 = []
for i in range(n):
    list1.insert(i, int(input()))
sum = 0
# method 1
print(list1)
for i in list1:

    sum = sum+i
print(sum)
# method 2
print(sum(list1))

# method 3
from functools import reduce
x=reduce(lambda x,y:x+y,list1)

print(x)
# # a = [1,2,3,4,5]
# # x= a.append(-3)
# print(type(list1[i]))
