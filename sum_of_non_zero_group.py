''' Question No. 74 (Practise set-3) '''
li=input("Enter Element in list followed by backspace-\t").split(" ")
li=[3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7]

for i in range(len(li)):
        li[i]=int(li[i])
nli=[]
s=0
for i in li:
    if i!=0:
        s=s+i
    else:
        if s!=0:
            nli.append(s)
        s=0

print(nli)
