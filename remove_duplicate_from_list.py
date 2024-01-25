''' Question No. 12 (Practise set-3)'''

n = int(input("How many element you want in your list-\t"))
list1 = []
for i in range(n):
    list1.insert(i, int(input()))

for i in list1:
    if list1.count(i) > 1 in list1:
        list1.remove(i)

print(list1)
