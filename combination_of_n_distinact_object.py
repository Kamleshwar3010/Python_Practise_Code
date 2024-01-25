''' Question No. 43 (Practise set-3) '''
import math


li=input("Enter Element in list followed by backspace-\t").split(" ")

for i in range(len(li)):
        li[i]=int(li[i])

nli=[]
# i=0
for i in li:
    temp=[]
    for j in li:
        if i!=j:
            temp.append(i)
            temp.append(j)
            if len(temp)==2:
                nli.append(temp)
                temp=[]
    if temp not in nli and temp!=[]:
        nli.append(temp)

print(nli)
