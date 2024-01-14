print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))

percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?" ))
people_to_split = int(input("How many people to split the bill? "))

pay_per_person = round(total_bill / people_to_split * (percentage_tip/100 + 1), 2)

print(f"Each person should pay: ${pay_per_person}")

