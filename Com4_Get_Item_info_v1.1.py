""" Component 4 of Price Checker Program
Create a looping code to ask for item name and price and weight
Use already created functions to check for valid inputs
input all items into lists for later use
Trial 1 is to get a working program
23/05/2022 Conor Smith"""


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


# taken from PC-Base_v1.py was created in component 1
# Main

# set up dictionary's and lists
product_name_list = []
product_amount_list = []
product_price_list = []

# Start of loop

# Initialize the loop so that it runs at least once
name = ""
count = 0
MAX_ENTRIES = 5

while name != "Xxx" and count != MAX_ENTRIES:
    # Get details
    name = not_blank("What is the product name?\n").title()
    if name != "Xxx":
        count += 1  # don't want to include testing Xxx
        product_name_list.append(name)
        # Get amount
        amount = float_check("How much is the item?\n$:")
        product_price_list.append(amount)
        quantity = float_check("What is the unit volume?\n:")
        product_amount_list.append(quantity)
# quantity = float_check(f"What is the unit volume?\n{unit_of_measure}:")
# unit_of_measure is already in base but requires many functions to work.
# Therefore, not using it for testing.
print(f"You have entered {count} products.")
print(product_name_list)
print(product_price_list)
print(product_amount_list)
# print statements are for testing
