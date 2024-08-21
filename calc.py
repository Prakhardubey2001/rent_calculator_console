## Inputs needed from the user
# Total Input
# Total Food Ordered
# Electricity units Spend
# Charge Per Unit
# Persons living in room/flat

## Output
# Rent Amount Payable

rent = float(input("Enter your hostel/flat rent amount: "))
food = float(input("Enter the food you are ordering for a month: "))
electricity_spend = float(input('Please enter how many units of electricity you will be using in one month: '))
charge_per_unit = float(input('Please enter how much it costs to charge each unit of electricity: '))
persons = int(input("Enter the number of persons living in your hostel/flat: "))

total_electricity_bill = electricity_spend * charge_per_unit
rent_amount = (rent + food + total_electricity_bill) / persons

# Print the amount payable with two decimal places and Indian Rupee symbol
print(f'The amount payable for rent per person per month is ₹ {rent_amount:.2f}')

