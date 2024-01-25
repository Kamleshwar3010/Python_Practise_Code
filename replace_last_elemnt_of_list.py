''' Question No. 33 (Practise set-3)'''
li = []
n = int(input("How many elemnt you want in list- \t"))
for i in range(n):
    li.append(int(input()))

li2 = []
n = int(input("How many elemnt you want in list 2- \t"))
for i in range(n):
    li2.append(int(input()))

li.remove(li[-1])
for i in li2:
    li.append(i)
print(li)
