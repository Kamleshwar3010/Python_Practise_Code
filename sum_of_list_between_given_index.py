''' Question No. 64 (Practise set-3) '''
li=input("Enter Element in list followed by backspace-\t").split(" ")

for i in range(len(li)):
        li[i]=int(li[i])

L=int(input("give lower index-\t"))
U=int(input("give upper index-\t"))
s=0
for i in range(L,U+1):
    s+=li[i]

print(s)
