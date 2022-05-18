""" Component 2 of Price Checker Program
Ask user if used program before if so continue to program,
if not display instructions
V1 is to create function to check for yes/no responses
17/05/2022 Conor Smith"""


# function that only allows yes or no responses
def yes_no_checker(question):
    response = ""
    while response != "yes" and response != "no":
        response = input(question).lower()
    if response == "yes":
        return True
    elif response == "no":
        return False


# Main routine
display_instructions = yes_no_checker("Have you used this program before?"
                                      "\n(yes/no)\n")
