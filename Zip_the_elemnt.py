''' Question No. 50 (Practise set-3) '''
n=int(input("how many sublist you want in list-1-\t"))
li=[]
l=[]
for i in range(n):
    n=int(input(f"how many element you want in sublist {i+1}\t"))
    temp=[]
    for j in range(n):
        temp.append(int(input("enter value-\t")))
    li.append(temp)
n=int(input("how many sublist you want in list-2-\t"))
for i in range(n):
    n=int(input(f"how many element you want in sublist {i+1}\t"))
    temp=[]
    for j in range(n):
        temp.append(int(input("enter value-\t")))
    l.append(temp)
nli=[]
# p=list(zip(li,l))
for i in range(len(li)):
    temp=[]
    temp.append(li[i])
    temp.append(l[i])
    t=[]
    for j in range(len(temp)):
        for k in temp[j]:
            t.append(k)
    nli.append(t)

print(nli)
