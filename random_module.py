import random as r
# for i in range(5):
#     x=r.randint(5,50)
#     print(x)
# for i in range(5):
#     x=r.r()
#     print(x)

# for i in range(5):
#     r.seed(10)
#     x=r.r()
#     print(x)

# for i in range(5):
#     x=r.getrandbits(3)
#     print(x)

# for i in range(5):
#     x=r.randrange(5,50,3)
#     print(x)

# mylist = ["apple", "banana", "cherry","Mango"]
# print(r.sample(mylist,k=2))

# my_list = [1, 2, 3, 4, 5]
# r_e = r.choice(my_list)
# print(r_e)

# fruits = ['apple', 'banana', 'orange', 'pear','Mango']
# w = [0.3, 0.2, 0.3, 0.2,0.4]
# c_w = [0.9, 0.5, 0.8, 0.7,0.3]
# # selected_fruits = r.choices(fruits,weights=w,cum_weights=c_w, k=10)
# selected_fruits = r.choices(fruits,weights=w, k=10)
# print(selected_fruits)
# selected_fruits = r.choices(fruits,cum_weights=c_w, k=10)
# print(selected_fruits)

# ''' Question no. 18 (Practise set-3)'''
# fruits = ['apple', 'banana', 'orange', 'pear','Mango']
# r.shuffle(fruits)
# print(fruits)
# for i in range(5):
#     x=r.uniform(20, 60)
#     print(x)
# print(r.r())

# state = r.getstate()
# print(f"state-{state}\n")
# print(r.r())
# r.setstate(state)
# print(f"state-{state}\n")
# print(r.r())

state = r.getstate()
x = r.randint(1, 10)
y = r.uniform(0, 1)
print(f"x- {x},y- {y}")
r.setstate(state)
x_again = r.randint(1, 10)
y_again = r.uniform(0, 1)
print(f"x after- {x_again},y after- {y_again}")
print(x == x_again)  # output-> True
print(y == y_again)  # output-> True
