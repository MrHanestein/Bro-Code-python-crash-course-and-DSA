# Python Calculator beginner level program.

Operators = input("Pick an operator from the following (* + - / %):")
number1 = float(input("Pick a number between 1 to 50:"))
number2 = float(input("Pick a number between 51 to 100:"))

# Use if conditional statement with string literals
if Operators == "*":
    Multiplication = number1 * number2
    print(Multiplication)
elif Operators == "+":
    Addition = number1 + number2
    print(Addition)
elif Operators == "-":
    Subtraction = number1 - number2
    print(Subtraction)
elif Operators == "/":
    Division = number1 / number2
    print(Division)
elif Operators == "%":
    Modulus = number1 % number2
    print(Modulus)
else:
    print(f"Your selected operator: {Operators} is invalid, Try again!!")
