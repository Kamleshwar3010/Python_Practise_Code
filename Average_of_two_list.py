''' Question No. 57 (Practise set-3) '''

li=input("Enter Element in list-1 followed by backspace-\t").split(" ")

for i in range(len(li)):
        li[i]=int(li[i])
l=input("Enter Element in list-2 followed by backspace-\t").split(" ")

for i in range(len(l)):
        l[i]=int(l[i])

print(f"Average of two list-\t{(sum(li)+sum(l))/(len(li)+len(l))}")
