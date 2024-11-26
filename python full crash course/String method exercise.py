# Validate user input exercise
# Requirements/conditions:
# 1. The username must not exceed 12 characters
# 2. The username must not contain spaces
# 3. The username must not contain digits

# Requirement 1.
# Step 1 - assign input() function to a variable/container
username = input("Enter your username:")

# Step 2 - Use an if-else statement.
if len(username) > 12:
    print("Your username must not exceed 12 characters!")
else:
    print(f"Welcome {username}!")

# Requirement 2
# username.find("") == -1. This finds the spaces in the variable and returns -1 if there are no spaces
# not inverses the end result of "True". So it becomes the opposite being false
if not username.find(" ") == -1:
    print(f"Your username: {username} cannot contain spaces")
else:
    print(f"Your username is appropriate {username}")
    print(f"{username}, please ensure they are no digits")

# Requirement 3
# username with isalpha() function
# Use the not function to inverse true to false
if not username.isalpha():
    print("Your username cannot contain digits")
else:
    print(f"Your username contains no digits, welcome again {username}")
