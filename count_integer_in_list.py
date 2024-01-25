''' Question No. 58 (Practise set-3) '''
li=input("Enter Element in list followed by backspace-\t").split(" ")

for i in range(len(li)):
        li[i]=int(li[i])

count=0
for i in li:
    if isinstance(i,int)==True:
        count+=1

print(count)
