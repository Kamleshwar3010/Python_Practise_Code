''' Question No. 45 (Practise set-3) '''
li=input("Enter Element in list followed by backspace-\t").split(",")

for i in range(len(li)):
        li[i]=round(float(li[i]))

print(f"Minmum- {min(li)}")
print(f"Maximum- {max(li)}")
li.sort()
nli=list(map(lambda x:x*5,li))
s=set(nli)
print(nli)
