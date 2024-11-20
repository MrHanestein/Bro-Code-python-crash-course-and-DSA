# Simple Weight converter beginner Program
# Units in kilograms or pounds

Weight = float(input("Enter your current weight:"))
units = input("Pick the correct units (K or L):")

if units == "K":
    Weight /= 2.205
    units = "Kg"
elif units == "L":
    Weight *= 2.205
    units = "lbs"
else:
    print(f"Your selected Weight: {Weight} is invalid! Try again!")

print(f"Your current Weight is {round(Weight, 3)}{units}, thank you!")


