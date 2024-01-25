#practise question 21
print("Enter Number till which you want to continue series")
n=int(input())
i=2
sum=0
while(i<=n):
    sum+=(1/i)
    i=i+2
print(sum)
