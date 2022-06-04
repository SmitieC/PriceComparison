"""Base Component of Price Checker program
Include all components into one program
V3 resolve more issues related to usability testing
Conor Smith"""


# Functions go here
# Blank checker function
def not_blank(question):
    valid = ""
    # using .isalpha check for response
    while not valid.isalpha():
        valid = input(question)
        if valid == "" or valid[0].isalpha() != True:
            # changed to only query first position
            print("This cannot be blank...")
        else:
            return valid


# Number checker function
def num_check(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


# float checker function do not allow negative numbers
def float_check(question):
    while True:
        try:
            float_num = input(question)
            if float(float_num) < 0:
                print("please enter a positive number")
                # Create second loop to only allow positive numbers
            else:
                return float(float_num)
        except ValueError:
            print("please enter valid number:\n")


# function that only allows yes or no responses
def yes_no_checker(question):
    response = ""
    while response != "yes" and response != "no":
        response = input(question).lower()
    if response == "yes":
        return True
    elif response == "no":
        return False


# Function to check for unit of measure
def unit_check(question):
    error = "\nSorry, you must enter a valid unit of measure\n"
    unit = ""
    while unit != "l" and unit != "ml" and unit != "g" and unit != "kg":
        unit = input(question).lower()
        if unit == "ml" or unit == "l" or unit == "g" or unit == "kg":
            return unit
        else:
            print(error)


# Function to sort product_list by value
def best_value(value):
    return value[3]


# Main

# set up dictionary's and lists
product_list = []

# set up variables and constants
name = ""
count = 0
MAX_ENTRIES = 5
instructions = "***Instructions***\n" \
               "This program will compare and produce the best value items\n" \
               "based on the following criteria:\n" \
               "1. Price\n" \
               "2. Quantity\n" \
               "3. Budget\n" \
               "The program will then display the best value item \n"\
               f"The program will compare a max of {MAX_ENTRIES} items\n" \
               f"To exit early type 'xxx'\n"

# ask user if they have used the program before
# show instructions if they would like
name = not_blank("What is your name: ")
display_instructions = yes_no_checker("Have you used this program before?"
                                      "\n(yes/no)\n")
if display_instructions is False:
    print(instructions)
# Get budget and unit of measure
budget = float_check("What is your budget?\n$")
unit_of_measure = unit_check("what is your unit of measure\nl, ml, g, kg:")
# loop to get item info
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
        value = float(round(value, 2))  # round to 2 decimal places
        product_list.append([name, amount, quantity, value])
# Reorder list based on best value
product_list.sort(key=best_value)
# Print results to user
for i in range(len(product_list)):
    if product_list[i][1] < budget:
        print("***** Summary *****")
        print(f"You have entered {count} products")
        print("\nThe best value product is:")
        print(product_list[i][0], "at the price of: $", product_list[i][1])
        print(f"\nThe list sorted from best value to worst:\n(arranged name, "
              f"price, volume, value per {unit_of_measure})\n{product_list}")
        print("\nThank you for using this program!")
        break
    else:
        print("***** Summary *****")
        print(f"You have entered {count} products")
        print("\nSorry, there are no products within your budget")
        print(f"The list sorted from best value to worst:\n(arranged name, "
              f"price, volume, value per {unit_of_measure})\n{product_list}")
        print("\nThank you for using this program!")
        break
