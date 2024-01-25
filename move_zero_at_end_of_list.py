''' Question No. 34 (Practise set-3)'''
# li = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0,
#       0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
li = []
n = int(input("How many elemnt you want in list- \t"))
for i in range(n):
    li.append(int(input()))

for i in li:
    if i == 0:
        li.append(i)
        li.remove(i)

print(li)
