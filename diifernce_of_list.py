''' Question No. 32 (Practise set-3)'''
c1 = ["red", "orange", "green", "blue", "white"]
c2 = ["black", "yellow", "green", "blue"]
c1_minus_c2 = []
for i in c1:
    if i not in c2:
        c1_minus_c2.append(i)
c2_minus_c1 = []
for i in c2:
    if i not in c1:
        c2_minus_c1.append(i)

print(c1_minus_c2)
print(c2_minus_c1)
