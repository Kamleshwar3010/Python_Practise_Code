''' Question No. 23 (Practise set-3)'''
li = []
n = int(input("How many elemnt youy want in list-\t"))
for i in range(n):
    li.append(str(input()))
count = 0
for i in li:
    if len(i) > 1 and i[0].lower() == i[-1].lower():
        count += 1

print(f"Result: {count}")
