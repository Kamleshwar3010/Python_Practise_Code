''' Question No. 36 (Practise set-3) '''
li=input("Enter Element in list followed by backspace-\t").split(" ")

c=input("Enter the character to check")

nli=[]
for i in li:
    if i[0]==c:
        nli.append(i)

print(nli)
