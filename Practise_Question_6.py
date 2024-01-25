"""Write the pseudocode to print the bill depending upon the price and quantity of an item. Also print Bill GST, which is the bill after adding 5% of the tax to the total bill"""
items = int(input("How many items do you have? "))

total = 0
for i in range(items):
    qty = int(input(f"Enter quantity of item {i+1}: "))
    price = int(input(f"Enter price of item {i+1}: "))
    total += qty * price

gst = total * 0.05
final_bill = total + gst

print(f"Original bill: ${total:.2f}") #.2f is same as setprecision() in C++
print(f"Bill with 5% GST: ${final_bill:.2f}")
