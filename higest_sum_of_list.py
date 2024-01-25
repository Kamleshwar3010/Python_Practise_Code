''' Question No. 35 (Practise set-3) '''
n=int(input("how many list you want-\t"))

li=[]
for i in range(n):
    temp=[]
    s=int(input(f"how many element you want in list{i+1}-\t"))
    for j in range(s):
        temp.append(int(input()))
    li.append(temp)

print(f"Your List {li}")

n=0
temp=[]
for i in li:
    if n< sum(i):
        n=sum(i)
        temp=i

print(temp)
