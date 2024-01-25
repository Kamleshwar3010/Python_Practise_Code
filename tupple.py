my_tuple = ("Apple", [1, 2, 3, "five"], (8, 9, 10))

# my_tuple[0][1]=my_tuple[0][1].replace("p","z") # not supported
# print(my_tuple)

# my_tuple[1][0]=10 # to update list inside tupple
# print(my_tuple)

# my_tuple[1][3]=my_tuple[1][3].replace("five","six") # to change string in list inside tupple
# print(my_tuple)


# print(my_tuple[0][1]) # print 'p' of apple
# print(my_tuple[1][3][2]) # print 'v' of list in my_tuple

fruits = ("Apple", "Banana", "Cherry", "Kiwi", "Grapes")
# a,b,*c=fruits
# print(c) #--> cheery, kiwi,Grapes

# my_tuple = my_tuple+fruits
# print(my_tuple) # to extend tuple

# a,b,*c,d=fruits
# print(c) #--> cheery, kiwi
# print(d) #--> Grapes

# a,b,*c,d,e,f=fruits
# print(c) # -->[] i.e empty list
# print(d) # -->cheery
# print(e) # -->Kiwi
# print(f) # --> Grapes

# name=("Kamleshwar")
# print(type(name)) # --> tuple

# name=tuple("Kamleshwar") # it is a way to declear a tuple with single element
# name=("Kamleshwar",) # it is another way to declear a tuple with single element
# print(type(name)) #--> tuple

# lis=[1,2,3,"five"]
# lis[3]="f"+lis[3][1].replace("i","x")+"ve"
# print(lis)

list_1 = [1, 2, 3, 4, 5, 6]
tupple_1 = (1, 2, 3, 4, 5, 6)
# print(max(list_1)) #return max element of list
# print(min(list_1)) #return min element of list
# print(max(tupple_1)) #return max element of tuple
# print(min(tupple_1)) #return min element of tuple
print(list_1*2) # every element apper double time in list
