''' Question No. 48 (Practise set-3) '''
r=int(input("How many row you want-\t"))
c=int(input("How many column you want-\t"))
li=[]
for i in range(r):
    temp=[]
    for j in range(c):
        temp.append(int(input(f"enter {j+1}th element in {i+1}th row-\t")))
    li.append(temp)

s=0
for i in range(c):
    for j in range(r):
        s+=li[j][i]
    print(s)
    s=0
