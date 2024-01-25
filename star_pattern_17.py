# using while loop
# i = 1
# while (i < 7):
#     j = 6
#     k = 0
#     while (j > i):
#         print(" ", end="")
#         j = j-1
#     if i > 2 and i < 6:
#         while (k < i):
#             if k == 0 or k == i-1:
#                 print("*", end="")
#                 k = k+1
#             else:
#                 print(" ", end="")
#                 k = k+1
#     else:
#         while (k < i):
#             print("*", end="")
#             k = k+1
#     print("")
#     i = i+1

# using for loop
# for i in range(1, 7):
#     for j in range(6-i):
#         print(" ", end="")
#     if i > 2 and i < 6:
#         for k in range(i):
#             if k == 0 or k == i-1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#     else:
#         for k in range(i):
#             print("*", end="")
#     print("")
