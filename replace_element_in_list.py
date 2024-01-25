''' Question No. 27 (Practise set-3)'''
li = []
n = int(input("How many elemnt you want in list- \t"))
for i in range(n):
    li.append(int(input()))

print(f"orginal list- {li}")
for i in range(0, n-1, 2):
    temp = li[i]
    li[i] = li[i+1]
    li[i+1] = temp

print(f"Final List {li}")
