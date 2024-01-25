''' Question No. 42 (Practise set-3) '''
import random
li=input("Enter Element in list followed by backspace-\t").split(" ")

for i in range(len(li)):
        li[i]=int(li[i])
print(f"orignal list {li}")
n=int(input("how many elemnet you want to selected randomly-\t"))
print(f"Randomly selected list-\t{random.choices(li,k=n)}")
