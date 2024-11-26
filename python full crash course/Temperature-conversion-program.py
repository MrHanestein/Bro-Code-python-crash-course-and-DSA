# Simple temperature conversion program
# Temperature in Kelvin or celcius

Temp = input("Pick a temperature in (K or C):")
SelectedTemp = float(input(f"Enter the number for your selected temp:"))

if Temp == "C":
    SelectedTemp = 9 * SelectedTemp / 5 + 32
    print(f"Your selected temperature in fahrenheit is {SelectedTemp:.2f}")
elif Temp == "K":
    SelectedTemp = SelectedTemp - 32 * 5 / 9
    print(f"Your selected temperature in Celcius is {SelectedTemp:.2f}")

else:
    print(f"Your temperature: {Temp} is invalid. Try again!")