""" Component 1 of Price Checker Program
Set out Lists Variables and functions to then build on in future components
V3 is making a function to test for digit inputs
trying a different way to check for digits from version 2
10/05/2022 Conor Smith"""


# # Blank checker function
# def not_blank(question):
#     valid = ""
#     # using .isalpha check for response
#     while not valid.isalpha():
#         valid = input(question)
#         if valid == "" or valid.isalpha() != True:
#             print("This cannot be blank...")
#         else:
#             return valid


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
# removed blank checker main routine as it was not required for v3 testing
# name = not_blank("What is your name: ")
# using print statement to test the function
# print(f"Hello {name}!")
digit = num_check("How old are you: ")
