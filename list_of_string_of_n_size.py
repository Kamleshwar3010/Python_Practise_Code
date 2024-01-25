''' Question No. 55 (Practise set-3)'''

list1=input("Enter txt-\t").split(" ")
new_list = []
n = int(input("length of N-\t"))
for i in list1:
    if len(i) == n:
        new_list.append(i)

print(new_list)
