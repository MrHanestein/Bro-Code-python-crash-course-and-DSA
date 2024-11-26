# Logical Operators = (1. OR, 2. AND, 3. NOT)
# They are 3 operators and they evaluate for either one or more condition
# is true or false
# 1. OR operator - At least one of the two conditions must be true
# 2. AND operator - Both of the conditions must be true
# 3. NOT operator - Condition is either "not" false or "not" true.

# OR Operator Example
# Temperature in celcius
cold_temp = 3
hot_temp = 35

# Weather condition
is_cold = True
is_hot = False
is_burning = True

# Loops - If loops evaluates for two conditions.
# If loops with the OR operator
if cold_temp < 15 or is_cold:
    print("The weather is too cold to go out today")
else:
    print("The weather is suitable to go outing!")

# If loops with the AND Operator
if hot_temp > 30 and hot_temp > cold_temp and is_burning:
    print("The weather is boiling hot today!")
else:
    print("It is alright to go out today!")

# If loops using the (NOT + AND) Operator
if is_cold or cold_temp < hot_temp and not is_hot:
    print("The weather is appropriate")
    # if loops - elif
elif is_hot and not is_burning:
    print("The weather is not suitable to go out")
else:
    print("The weather has to be appropriate to go out today")


