''' Question No. 15 (Practise set-3)'''

n = int(input("How Many Element You Want In List 1-\t"))
list1 = []
for i in range(n):
    list1.insert(i, int(input(f"Enter {i+1}th value in list-\t")))
n = int(input("How Many Element You Want In List 2-\t"))
list2 = []
for i in range(n):
    list2.insert(i, int(input(f"Enter {i+1}th value in list-\t")))
print(f"list 1 is {list1}")
print(f"list 2 is {list2}")

new_list = []
if len(list1) > len(list2):
    n = len(list1)
    d = n-len(list2)
    for i in range(d):
        list2.append(0)
else:
    n = len(list2)
    d = n-len(list1)
    for i in range(d):
        list1.append(0)
for i in range(n):
    new_list.append(list1[i]-list2[i])
print(f"Differnce of two list is {new_list}")
