''' Question No. 17 (Practise set-3)'''

n = int(input("How Many Element You Want In List 1-\t"))
list1 = []
for i in range(n):
    list1.insert(i, int(input(f"Enter {i+1}th value in list-\t")))
even_list = []
[list1.remove(i) if i % 2 == 0 else even_list.append(i) for i in list1]
print(even_list)
