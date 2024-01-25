''' Question No. 47 (Practise set-3) '''
li=[]
for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(int(input(f"enter {j+1}th element in {i+1}th row-\t")))
    li.append(temp)

print(li)
