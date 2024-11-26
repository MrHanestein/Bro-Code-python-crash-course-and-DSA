# 13. String Methods - Using functions with string methods
# Imagine variables as containers to store strings.

# Example 1
# name is Container #1
name = input("What is your name?")
# result is Container #2 and len() is a function to count the index of a string
result = len(name)
print(result)

# Example 2 - String method functions

# Using an assigned variable with the name.__(Function) for string methods in an index.
# Find the index of "a"
# Index - An index starts from number 0 at the first letter. Example: David. Letter "D" is at index 0.
letter_a = name.find("a")
print(letter_a)

# rfind function
letter_v = name.rfind("v")
print(letter_v)

# .capitalize(), .upper(), .lower() function for string methods
variable_capitalize = name.capitalize()
variable_uppercase = name.upper()
variable_lowercase = name.lower()

# Return digits as a boolean method.
variable_Digit = name.isdigit()
print(variable_Digit)

# Alphanumerics function
variable_alpha = name.isalpha()
print(variable_alpha)

# Count function
# Example 3 - Phone number
phone_number = input("Write down your phone number: ")
number_count = phone_number.count("-")
print(number_count)

# replace function
# Example 4 - phone number

number_replace = phone_number.replace("-", "")
print(number_replace)