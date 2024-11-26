# While loops - Loop is executed as long as chosen condition remains true.
# Basically loop is infinite till condition is met.
# Escaping infinite loop: A true statement is needed to escape an infinite loop

first_name = input("What is your first name?")

# Loop would be infinite if first_name condition is not met.
# Empty string - ""
while first_name == "":
    print("You need to enter your first name!")
else:
    print(f"Welcome {first_name}")

# Example 2 - Age
Age = int(input(f"{first_name}. What is your age?"))

while Age < 0:
    print("Your age cannot be a negative number. Try again.")
else:
    print(f"{first_name}, your age is {Age}.")

# Example 3 - Using NOT operator in a while loop

pizza = input("Your favourite fast food pizza chain. (press E to exit)")

while not pizza == "e":
    print(f"Your favourite pizza chain is {pizza}")
    # Define another variable to continue the loop.
    food_continue = input("Enter another pizza chain you love. (Press E to exit)")
print("Thank you")

# Example 4 - Using the OR operator in a while loop

numbers = int(input("Enter a number between 1 - 20:"))

while numbers < 1 or numbers > 20:
    print(f"Your selected number:{numbers} is out of range")
    # Define another variable to continue the loop.
    num_continue = int(input("Enter more numbers between the range 1 - 10:"))
print("Thank you")
