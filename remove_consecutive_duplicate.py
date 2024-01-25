''' Question No. 37 (Practise set-3) '''
li=input("Enter Element in list followed by backspace-\t").split(" ")

for i in range(len(li)):
        li[i]=int(li[i])

for i in li:
        if i==li[li.index(i)+1]:
            li.remove(li[i])

print(li)
