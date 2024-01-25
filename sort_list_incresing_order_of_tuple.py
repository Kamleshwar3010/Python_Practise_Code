''' Question No. 24 (Practise set-3) '''
list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range(len(list1)):
    for j in range(i,len(list1)):
        if list1[i][1] > list1[j][1]:
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp


print(list1)
