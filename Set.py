# my_set_a = {1, 2, 3, [1, 8, "hi"]}  # we can not give list as set element
# print(my_set_a)
my_set = {1, 2, 3, 8, "hi", 1}
# print(my_set) # {1,2,3,8,"hi"}
a = set()
# print(a)
# print(type(a))
b = set([1, 2, 3, 4, 90, 67, 15])
# print(b)
c = b.copy()  # create copy of b in c
# print(c)
# print(type(c))
my_set.update(["hello", 11.9])
# print(my_set)
# a.add([19, 51, 66, 71]) # we can not give list as set element
a.add(19)
# print(a)
del a
# print(a) # raise error as set a is deleted
c.clear()
# print(c) # remain structure
# print(b.remove(69))  # raise error as 69 is not in set
# print(b.discard(69))  # does not raise error even 69 is not in set instead return "none"
# print(my_set | b) # union
# print(my_set & b) # Intersection
# print(my_set - b) # set difference
# print(my_set ^ b) # semmetric differnce
# print(my_set.isdisjoint(b)) # return false
# print(my_set.issubset(b)) # return false
# print(my_set.issuperset(b)) # return false


# frogen set
a = frozenset([1, 2, 3, 4, 6, 5, 7, 5])
# print(a)
# print(type(a))

print(max(b))  # return max elemnt of set
print(min(b))  # return min elemnt of set
print(len(b))  # return length elemnt of set
