""" Component 1 of Price Checker Program
Set out Lists Variables and functions to then build on in future components
V5 is making Variables to store Budget and user's name
10/05/2022 Conor Smith"""


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


# Main Routine
# Set up lists
product_name_list = []
product_amount_list = []
product_price_list = []
# list to store value from price over quantity calculation
product_value_list = []

# Set up variables
user_budget =   # need to make a float checker for money

name = not_blank("What is your name: ")
digit = num_check("How old are you: ")

