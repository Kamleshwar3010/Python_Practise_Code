'''Enter the unique value in list till user enter the no 0 '''
list=[]
num=int(input("Enter the num :"))
while(num!=0):
    if num not in list:
        list.append(num)
        list.sort()
    else:
        continue
    num=int(input("Enter the number"))

print(list)
