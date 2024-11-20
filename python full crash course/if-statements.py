# If conditional statements:
# if (condition): print("")
# elif (condition): print("")
# else: print("")

age = int(input("Enter your current age: "))
if age < 18:
    print("You are a minor, no entry!!!")
elif age >= 31:
    print("You are eligible, free shots!!")
else:
    print("Unidentified, no entry!!")

# 2. If with Strings. if condition == "" : print("")
name = input("Enter your new name: ")

if name == "Mike":
    print("Your new assigned name is now Mike!")
else:
    print("Enter Mike as you new name!")

# 3. If with Booleans. if condition: print("").
online = True
if online:
    print("Mike is currently online")
else:
    print("Mike is currently offline")