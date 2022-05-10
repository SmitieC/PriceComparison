""" Component 1 of Price Checker Program
Set out Lists Variables and functions to then build on in future components
V1 is making a function to test for blank inputs
6/05/2022 Conor Smith"""


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


# Main Routine
name = not_blank("What is your name: ")
# using print statement to test the function
print(f"Hello {name}!")
