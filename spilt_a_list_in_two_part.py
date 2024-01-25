''' Question No. 41 (Practise set-3) '''
li=input("Enter Element in list followed by backspace-\t").split(" ")

for i in range(len(li)):
        li[i]=int(li[i])

n=int(input("how many elemnent are in first list-\t"))

nli=[]
# for i in range(len(li)):
#     temp=[]
#     if i<n:
#         for j in range(n):
#             temp.append(li[i])
#     else:
#         for j in range(len(li)-n):
#             temp.append(li[i])
#     nli.append(temp)
i=0
while(i<len(li)):
    temp=[]
    if i<n:
        for j in range(n):
            temp.append(li[i])
            i=i+1
    else:
        for j in range(len(li)-n):
            temp.append(li[i])
            i=i+1
    nli.append(temp)


print(nli)
