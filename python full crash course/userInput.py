# Input function - input()
current_age = input("What is your current age")
print(f"My current age is {current_age}")

# Use of type casting in user input
cost_of_shoes = input("What is the cost of your shoes")
# Type cast to float
cost_of_shoes = float(cost_of_shoes)

# Return cost of shoes
cost_of_shoes += 1.1
print(f"New cost of shoe is ${cost_of_shoes}")

# Example 2
cost_of_bag = float(input("What is the cost of your bag"))
cost_of_bag += 1
print(f"New cost of bag is ${cost_of_bag}")

# Exercise 1 - Area of a Rectangle
# Area = Length * Width
length = float(input("Enter the length: "))
width = float(input("Enter the length: "))
Area = length * width

print(f"The area of the Rectange is {Area}cm")

# Exercise 2 - Shopping cart program (Item, Quantity, Total price).
Item = input("What item would you like to purchase?")
Quantity = int(input("How many items would you like to purchase?"))
price = float(input("What is the price?"))
total_cost = price * Quantity

print(f"Your selected item is a {Item} with {Quantity} in quantity")
print(f"The total cost is ${total_cost}")