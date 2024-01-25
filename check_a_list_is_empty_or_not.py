''' Question No. 2 (Practise set-3) '''
n = int(input("How many element you want in your list-\t"))
list1 = []
for i in range(n):
    list1.insert(i, int(input()))

if len(list1) == 0:
    print("List is Empty")
else:
    print(f"List have {len(list1)} element")
