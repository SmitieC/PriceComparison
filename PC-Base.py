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


# Main

# set up dictionary's and lists

# ask user if they have used the program before
# show instructions if they would like

# Get name (cannot be blank)
name = not_blank("What is your name: ")
# Get budget (cannot be blank, must be a number)
budget = float_check("What is your budget?\n$")
# loop to get item info

# Calculate best value

# Print results to user
