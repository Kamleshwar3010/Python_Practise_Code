'''Write an algorithm for this problem: Ram shewak goes to the market to buy some fruits and vegetables. He has a currency of Rs 500 with him for marketing. From a shop he purchases 2.0 kg Apple priced at Rs. 50.0 per kg, 1.5 kg Mango priced at Rs.35.0 per kg, 2.5 kg Potato priced at Rs.10.0 per kg, and 1.0 kg Tomato priced at Rs.15 per kg. He gives the currency of
Rs. 500 to the shopkeeper. Find out the amount shopkeeper will return to Ramshewak. and also tell the total item purchased.'''
Money = 500
for i in range(4):
    item = str(input("Enter the Name of item- "))
    Qty = float(input("Enter the Quantity- "))
    Price = int(input("Enter Price for one Kg- "))
    Money = Money-(Price*Qty)

print(f"Your Remaining {Money} and {i+1} no. of item you purchased")
