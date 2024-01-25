''' Question No. 63 (Practise set-3) '''
from functools import reduce


li=input("Enter Element in list followed by backspace-\t").split(" ")

for i in range(len(li)):
        li[i]=int(li[i])

print(reduce(lambda x,y:x*y,set(li)))
