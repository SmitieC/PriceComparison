""" Component 4 of Price Checker Program
Create a looping code to ask for item name and price and weight
Use already created functions to check for valid inputs
Sort list by value
28/05/2022 Conor Smith"""


# unit checker from base component
def unit_check(question):
    error = "\nSorry, you must enter a valid unit of measure\n"
    unit = ""
    while unit != "l" and unit != "ml" and unit != "g" and unit != "kg":
        unit = input(question).lower()
        if unit == "ml" or unit == "l" or unit == "g" or unit == "kg":
            return unit
        else:
            print(error)


# not blank function taken from base
def not_blank(question):
    valid = ""
    # using .isalpha check for response
    while not valid.isalpha():
        valid = input(question)
        if valid == "" or valid.isalpha() != True:
            print("This cannot be blank...")
        else:
            return valid


# float check taken from previous component
def float_check(question):
    while True:
        try:
            float_num = input(question)
            return float(float_num)

        except ValueError:
            print("please enter valid number:\n")


def best_value(value):
    return value[3]


# taken from PC-Base.py was created in component 1
# Main

# set up a 2 dimensional list
product_list = []

# Start of loop
# Initialize the loop so that it runs at least once
name = ""
count = 0
MAX_ENTRIES = 5
unit_of_measure = unit_check("what is your unit of measure\nl, ml, g, kg:")

while name != "Xxx" and count != MAX_ENTRIES:
    if MAX_ENTRIES - count > 1:
        print(f"You have {MAX_ENTRIES - count} entries left.")
    else:
        # warn user of final product
        print("\n***You have ONLY ONE product left!***")
    # Get details
    # input all details into a new sub-list for each loop of inputs
    name = not_blank("What is the product name?\n").title()
    if name != "Xxx":
        count += 1  # don't want to include testing Xxx
        # Get amount
        amount = float_check("How much is the item?\n$:")
        # Get unit volume
        quantity = float_check(f"What is the unit volume?\n{unit_of_measure}:")
        # calculate product value
        value = amount / quantity
        product_list.append([name, amount, quantity, value])

print(f"This is your unsorted list\n{product_list}")
product_list.sort(key=best_value)
print(f"This is your sorted list\n{product_list}")
# print statements are for testing
