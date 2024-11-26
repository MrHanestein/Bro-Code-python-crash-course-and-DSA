# String Indexing - [Start : end : step]
# Example 1 - number = 0123456789
# start - 0 (index 1)
# end - 9 (index 10)
# Condition - ([start:end])

credit_number = "0123456789"
print(credit_number[0])
print(credit_number[1])
print(credit_number[2])
print(credit_number[3])
print(credit_number[4])

# print first 4 indexes
print(credit_number[:4])

# print index 5 - 9
print(credit_number[5:9])

print(credit_number[-1])

# Prints by 2 steps.
print(credit_number[::2])

# Prints by 3 steps.
print(credit_number[::3])

# Quick exercise:
# Print a program for the last 4 digits of a credit card ONLY.
last_4digits = "1234-5678-9120-2134"
print(f"XXXX-XXXX-XXXX-{last_4digits[-4:]}")