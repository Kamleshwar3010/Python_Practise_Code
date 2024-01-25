''' Question No. 5 and 6 (Practise set-3)'''
import sys

# Method-1 (Using Pre-Define Method)
n = int(input("How many element you want in your list-\t"))
list1 = []
for i in range(n):
    list1.insert(i, int(input()))
# Method-1
print(f"Largest Value in List is {max(list1)}")
print(f"Smallest Value in List is {min(list1)}")

# Method-2
min_int = sys.maxsize
max_int = -sys.maxsize-1
for i in range(len(list1)):
    if list1[i] > max_int:
        max_int = list1[i]
    if list1[i] < min_int:
        min_int = list1[i]

print(f"Largest Value in List is {max_int}")
print(f"Smallest Value in List is {min_int}")
