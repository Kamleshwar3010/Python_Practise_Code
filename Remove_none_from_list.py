'''Question No. 67 (Practise set-3)'''
# li=[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
li=input("Enter Element in list followed by backspace-\t").split(" ")

# for i in range(len(li)):
#     if li[i].capitalize()=="None":
#         li.remove(li[i])
#     else:
#         li[i]=int(li[i])
for i in li:
    if i.capitalize()=="None":
        li.remove(i)
for i in range(len(li)):
       li[i]=int(li[i])

print(li)
