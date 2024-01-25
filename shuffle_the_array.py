''' Question no. 18 (Practise set-3)'''
import random
li=input("Enter Element in list followed by backspace-\t").split(" ")

for i in range(len(li)):
        li[i]=int(li[i])
print(f"orignal list {li}")
random.shuffle(li)
print(f"shuffled list -{li}")
