''' Question No. 46 (Practise set-3) '''
r=int(input("How many row you want-\t"))
c=int(input("How many column you want-\t"))
li=[]
for i in range(r):
    temp=[]
    for j in range(c):
        temp.append(0)
    li.append(temp)

print(li)
