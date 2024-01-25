''' Question No. 7 and 8 (Practise set-3)'''
import sys


# Method-1 (Using Pre-Define Method)
n = int(input("How many element you want in your list-\t"))
list1 = []
for i in range(n):
    list1.insert(i, int(input()))
# Method-1
smax = min(list1)
smin = max(list1)
for i in list1:
    if i < max(list1) and i > smax:
        smax = i
    if i > min(list1) and i < smin:
        smin = i
print(f"Second Largest Value in List is {smax}")
print(f"Second Smallest Value in List is {smin}")

# # Method-2
min_int = sys.maxsize
max_int = -sys.maxsize-1
for i in range(len(list1)):
    if list1[i] > max_int:
        max_int = list1[i]
    if list1[i] < min_int:
        min_int = list1[i]

smax1 = min_int
smin1 = max_int
for i in list1:
    if i < max_int and i > smax1:
        smax1 = i
    if i > min_int and i < smin1:
        smin1 = i
print(f"Second Largest Value in List is {smax1}")
print(f"Second Smallest Value in List is {smin1}")
