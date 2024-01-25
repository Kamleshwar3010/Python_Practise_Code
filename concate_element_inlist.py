li = ["p", "q"]
''' Question No. 26 (Practise set-3)'''
n = int(input("Enter range-\t"))
new_list = []
for i in range(1, n+1):
    for j in range(len(li)):
        new_list.append(li[j]+str(i))

print(new_list)
