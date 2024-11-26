# Compound Interest Calculator Program.
# Compound interest formula - A = P(1 + r/n) ^ t
# n = 100
# A = final amount
# P = Initial principal balance
# r = Interest rate (Float type)
# t = number of time periods elapsed

# Using a nested if loop inside a while loop:
principal = 0
rate = 0
time = 0
# Keeps looping if number is less than or equal to 0
# While true:
while principal <= 0:
    principal = int(input("Enter principal amount: "))
    # nested if-else loop:
    if principal <= 0:
        print("Your principal value cannot be less than or equal to 0!")


# Interest rate
while rate <= 0:
    # Type cast interest rate to float data type
    rate = float(input("Enter the Interest rate: "))
    # nested if-else loop:
    if rate <= 0:
        print("Your Interest rate cannot be less than 0!")

# Time
while time <= 0:
    time = int(input("Enter the time spent in years: "))
    # nested if-else loop:
    if time <= 0:
        print("Time cannot be less than or equal to 0!!!")

print("The following are your chosen values:")
print(principal)
print(rate)
print(time)

# Power function - pow()
Compound_Interest = principal *  pow((1 + rate / 100), time)
# Compound interest rate
Compound_final_interest = print(f"Your Balance after {time} years is ${Compound_Interest:.2f}. Thank you!")
print(Compound_final_interest)

# Using a Break statement under a while loop.
is_dark = False

while True:
    print(is_dark)
    if is_dark:
        print("It is dark")
    else:
        break
print(input("Is it Dark (Type:yes/no)"))
