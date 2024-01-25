#Practise Question 14
num=int(input("Enter The Number-"))
orgnum=num
sum=0
while(num>0):
    temp=(num%10)**3
    sum=sum+temp
    num=num//10

if(orgnum==sum):
    print(orgnum," is aramstrong no.")
else:
    print(orgnum," is not an aramstrong no.")
