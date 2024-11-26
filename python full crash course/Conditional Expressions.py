# Conditional Expressions - One-line shortcut for the if - else
# Statements

# I would show an example of the normal representation and conditional representation
# Example 1:Normal representation of an if-else statement is:
age = 16
if age < 18:
    print("You are a minor!")
else:
    print("You are legal.")

# Example 1:Conditional expression representation of an if-else statement is:
age = 16 if age < 18 else "You are legal."

# Example 2: Encapsulating a conditional expression in a print statement
print("Donald Trump" if age > 60 else "Kamala")

# Formula (Conditional expressions):
# Formula: X (If - else statement) Y
# Explanation: Return first variable (X) if conditional statement is met.
# Else return second variable (Y).

# Example 3: Maximum and Minimum numbers.
max_num = 20
min_num = 18

legal_adult = max_num if max_num > min_num else "Minor"

# Example 4
# NOTE - If-else statements can use "String" and numerical expressions.
temperature = 34

Weather = "COLD" if temperature < 34 else "The weather is HOT"
