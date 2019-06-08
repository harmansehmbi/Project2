# Conditional Constructs
# Where we wish to check some Rules or Constraints

total = 500
discount = 40

# Leader if else

if total >= 100 and total < 200:
    print("Flat 20% Off")
elif total >=200 and total < 500:
    print("Flat 30% Off")
elif total >= 500:
    print("Flat 50% Off")
else:
    print("Please add valuable of upto 100 for Discount")

# Test Case