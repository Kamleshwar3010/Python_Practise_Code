''' Question No. 56, 60 (Practise set-3) '''
li=input("Enter Element in list followed by backspace-\t").split(" ")

for i in range(len(li)):
        li[i]=int(li[i])
nli=[]
for i in range(len(li)-1):
    nli.append(li[i+1]-li[i])

print(nli)
