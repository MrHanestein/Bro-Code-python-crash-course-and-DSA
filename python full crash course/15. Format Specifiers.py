# Format Specifiers - {value:flags} -


# flag example as a 2 significant figure.
shoe_price = 35.9998985938
bag_price = -20
house_price = 20000420000.0999530593
# flag spaces {:4} - pad with 4 spaces
print(f"Your shoe price is {shoe_price:.4f}")
print(f"Your shoe price is {shoe_price:.3f}")
print(f"Your shoe price is {shoe_price:.2f}")
print(f"Your shoe price is {shoe_price:.1f}")
# flag character line placement {:>} {:<} {:^}
angles = "Price point angles for shoes"
print(f"Your shoes price is at the right angle {shoe_price:>}")
print(f"Your shoes price is at the middle angle {shoe_price:^}")
print(f"Your shoes price is at the left angle {shoe_price:<}")
# flag symbol placement for mathematical expressions - use "-"
print(f"Your shoes price is at the right subtraction angle {shoe_price:-}")
print(f"Your shoes price is at the right addition angle {shoe_price:+}")
# flag symbol placement for comma placement - use ","
comma = ","
print(f"Your shoes price is a comma {shoe_price:,}")
# flag combination of "+,.2f"
print(f"Your shoes price is a comma {shoe_price:+,.5}")
