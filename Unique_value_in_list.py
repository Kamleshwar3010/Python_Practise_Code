''' Question No. 9 (Practise set-3)'''

n = int(input("How Many Element You Want In List-\t"))
list1 = []
for i in range(n):
    list1.insert(i, int(input(f"Enter {i+1}th value in list-\t")))

unique_value = set(list1)
print(unique_value)
