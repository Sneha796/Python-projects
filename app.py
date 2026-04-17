item = input("What item would you like to buy? : ") 
price = float(input(" What is the price of an item? : ")) 
quantity = int(input("How many item would you like to buy? :")) 
total = price * quantity

print(f"You have bought {quantity} * {item}")
print (f"Your total is: {total}") 
