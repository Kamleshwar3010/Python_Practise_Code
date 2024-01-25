''' Question No. 31 (Practise set-3)'''
# li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
li = []
n = int(input("How many elemnt you want in list- \t"))
for i in range(n):
    li.append(int(input()))

n = int(input("Enter the diffrence of element- \t"))

new_list = []
for i in range(n+1):
    temp = []
    for j in range(i, len(li), n+1):
        temp.append(li[j])
    new_list.append(temp)

print(new_list)
