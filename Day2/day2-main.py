total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = total_bill * (tip_percentage / 100)
amount_to_pay = (total_bill + tip) / people

print(f"Each person should pay ${amount_to_pay:.2f}")