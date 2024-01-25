''' Question No. 59 (Practise set-3) '''

li=input("Enter Element in list followed by backspace-\t").split(" ")

for i in range(len(li)):
        li[i]=int(li[i])
m=li.count(li[0])
for i in li:
    if li.count(i)>m:
        m=li.count(i)
for i in li:
    if li.count(i)==m:
        print(i)
    break
