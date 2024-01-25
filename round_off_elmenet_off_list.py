''' Question No. 44 (Practise set-3) '''
li=input("Enter Element in list followed by backspace-\t").split(" ")

for i in range(len(li)):
        li[i]=round(float(li[i]))

print(sum(li)*len(li))
