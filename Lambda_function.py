from functools import reduce


add = lambda a, b : a + b
# print(add(3,6))

'''Programe to multiply a no with unkown no'''
def compute(n):
    return lambda x:x*n

result=compute(2) # hold value compute
# print(result)
# print(result(15)) # calculate lambda function

y=lambda y:y*2
# print(y(2))

l1=[1,2,3,4,5,6,7,8,9,10]
nl=list(filter(lambda x:x%2==0,l1))# if value in list even then return the list value with even no
nt=tuple(filter(lambda x:x%2==0,l1))# if value in tupple even then return the list value with even no
ns=set(filter(lambda x:x%2==0,l1))# if value in set even then return the list value with even no
# nd=dict(filter(lambda x:x%2==0,l1))# raise error as it not have key value pair
# print(nl)
# print(nt)
# print(ns)
# print(nd)

nl1=list(map(lambda x:x*2,l1)) # double every value in list
# print(nl1)

li=list(filter(lambda y:y%2==0,map(lambda x:x*3,l1))) # return triple value of list element if elment is even
# print(li)

# def product(x,y):
#     return x*y

# ans = reduce(product, l1) # multiply every element with each other in list
# print(ans)

l2=[1,2,3,4,5]
print(reduce(lambda a, b: a+b, l2)) # give the sum of list
