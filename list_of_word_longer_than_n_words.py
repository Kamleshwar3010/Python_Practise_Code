''' Question No. 13 (Practise set-3)'''

list1=input("Enter txt-\t").split(" ")
new_list = []
n = int(input("length of N-\t"))
for i in list1:
    print(i)
    if len(i) > n:
        new_list.append(i)

print(new_list)
