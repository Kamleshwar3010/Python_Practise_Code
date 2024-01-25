''' Question No. 11 (Practise set-3) '''
list1 = input("Enter Element in list followed by backspace-\t").split(" ")
for i in range(len(list1)):
    if i==" ":
        break
    else:
        list1[i]=int(list1[i])

R1=int(input("Enter Lower range-\t"))
R2=int(input("Enter Upper range-\t"))

count=0
for i in list1:
    if i>=R1 and i<=R2:
        count=count+1

print(count)
