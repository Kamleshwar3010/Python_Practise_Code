''' Question No. 28 (Practise set-3)'''
li = []
n = int(input("How many elemnt you want in list- \t"))
for i in range(n):
    li.append(int(input()))

single_value = ""
for i in li:
    single_value += str(i)

print(int(single_value))
