"""Write an algorithm to display the total water bill charges of the month depending upon the number of units consumed by the customer as per the following criteria:
1 for the first 100 units @ Rs. 5 per unit
2 for next 150 units @ Rs. 10 per unit
3 more than 250 units @ Rs. 20 per unit
Also add meter charges of Rs. 75 per month to calculate the total water bill.
"""
bill = 0
total_unit = int(input("Enter the number of unit consumbed by user- "))
print("Fixed charge ---------------------- 75")
if total_unit <= 100:
    bill = 75+(total_unit*5)
    print(f"For {total_unit} unit is {total_unit*5} @ Rs.5")
    print(f"Total Bill ---------------------- {bill}")
elif total_unit <= 250:
    bill = 75+((total_unit-100)*10)+500
    print("First 100 unit is charged Rs.500 @ Rs.5")
    print(
        f"For Next {total_unit-100} unit is {(total_unit-100)*10} @ Rs. 10 per unit")
    print(f"Total Bill ---------------------- {bill}")
else:
    bill = 75+((total_unit-250)*20)+2000
    print("First 100 unit is charged Rs.500 @ Rs.5")
    print("For Next 150 unit is 1500 @ Rs. 10 per unit")
    print(
        f"For Remaining {total_unit-250} unit is {(total_unit-250)*20} @ Rs. 20 per unit")
    print(f"Total Bill ---------------------- {bill}")


"""
700-100=600     251-100=151
600-150=450     151-150=1

450*20=9000     100*5=500
150*10=1500     150*10=1500
100*5=500       1*20=20
75              75
"""
