''' Question No. 51 (Practise set-3) '''
n=int(input("how many sublist you want in list-1-\t"))
li=[]
for i in range(n):
    n=int(input(f"how many element you want in sublist {i+1}\t"))
    temp=[]
    for j in range(n):
        temp.append(int(input("enter value-\t")))
    li.append(temp)

temp=[]
for i in li:
    temp.append(len(i))
for i in li:
    if len(i)==max(temp):
        print(f"Maximum length- {tuple([max(temp),i])}")
    if len(i)==min(temp):
        print(f"Minimum length- {tuple([min(temp),i])}")
