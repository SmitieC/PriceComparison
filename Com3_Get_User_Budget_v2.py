""" Component 3 of Price Checker Program
Ask user for their budget and also for unit of measure
Use already made functions to check that answers are valid
V2 is to ask for users unit of measure
20/05/2022 Conor Smith"""


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


unit_of_measure = input("what is your unit of measure")
