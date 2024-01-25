''' Question No. 14 (Practise set-3)'''

n = int(input("How Many Element You Want In List 1-\t"))
list1 = []
for i in range(n):
    list1.insert(i, int(input(f"Enter {i+1}th value in list-\t")))
n = int(input("How Many Element You Want In List 2-\t"))
list2 = []
for i in range(n):
    list2.insert(i, int(input(f"Enter {i+1}th value in list-\t")))

for i in list1 and list2:
    if i in list1 and list2:
        print(f"{i} is common in both list")
