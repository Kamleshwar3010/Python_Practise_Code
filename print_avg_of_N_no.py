#Accept num till the user enter zero then find average
print("Enter Number",end="- ")
i=0
sum=0
num=int(input())
while(num!=0):
    sum+=num
    i=i+1
    num=int(input())
print(sum/i)
