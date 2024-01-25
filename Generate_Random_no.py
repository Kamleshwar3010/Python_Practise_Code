name1 = input()
i = sum = sum_1 = 0
list_1 = []
list_2 = []

while i < len(name1):
    list_1.append(ord(name1[i]))
    i = i + 1

name2 = input()
i = 0
while i < len(name2):
    list_2.append(ord(name2[i]))
    i = i + 1

for j in range(len(list_1)):
    sum += list_1[j]
for j in range(len(list_2)):
    sum_1 += list_2[j]
for j in range(1, 6):
    random_no = int(sum * sum_1 / list_1[j])
    print(random_no)
