"""Base Component of Price Checker program
Include all components into one program
Conor Smith"""


# Import Statements

# Functions go here
# Blank checker function
def not_blank(question):
    valid = ""
    # using .isalpha check for response
    while not valid.isalpha():
        valid = input(question)
        if valid == "" or valid.isalpha() != True:
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


# float checker function
def float_check(question):
    while True:
        try:
            float_num = input(question)
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


# Main

# set up dictionary's and lists
product_name_list = []
product_amount_list = []
product_price_list = []
# list to store value from price over quantity calculation
product_value_list = []

# set up variables and constants
instructions = "***Instructions***\n" \
               "This program will compare and produce the best value items\n" \
               "based on the following criteria:\n" \
               "1. Price\n" \
               "2. Quantity\n" \
               "3. Budget\n" \
               "The program will then display the best value item\n" \
               "Thank you for using this program!"

# ask user if they have used the program before
# show instructions if they would like
display_instructions = yes_no_checker("Have you used this program before?"
                                      "\n(yes/no)\n")
if display_instructions is False:
    print(instructions)
# Get budget (cannot be blank, must be a number)
budget = float_check("What is your budget?\n$")
# loop to get item info

# Calculate best value

# Print results to user
