# #you have to collect Rs.200 from all member of family
sum = 0
while (sum <= 200):
    money = int(input("Give Me Money "))
    if (money == 10 or money == 20 or money == 50):
        sum = sum+money
        last_amount = money
        if sum > 200:
            sum = sum-last_amount
            print(f"I want only {200-sum} Rs.")
        elif sum == 200:
            break
    else:
        print("Please Give Me Either 10,20 or 50 Rs.")
        continue
print("Yahoo", sum, "Rs. is collected")
