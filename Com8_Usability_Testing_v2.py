""" Component 8 of Price Checker Program
Fix minor errors in the program found through usability testing
V2 is to fix second set of errors
4/06/2022 Conor Smith"""

# round value to 2 decimal places before appending to list
amount = 12124
quantity = 12
value = amount / quantity
print(value)
value = float(round(value, 2))  # round to 2 decimal places
print(value)
