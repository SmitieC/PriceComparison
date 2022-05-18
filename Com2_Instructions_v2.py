""" Component 2 of Price Checker Program
Ask user if used program before if so continue to program,
if not display instructions
V2 receive response from function. continue if yes and print instructions if no
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
instructions = "***Instructions***\n" \
               "This program will compare and produce the best value items\n" \
               "based on the following criteria:\n" \
               "1. Price\n" \
               "2. Quantity\n" \
               "3. Budget\n" \
               "The program will then display the best value item\n" \
               "Thank you for using this program!"
display_instructions = yes_no_checker("Have you used this program before?"
                                      "\n(yes/no)\n")
if display_instructions is False:
    print(instructions)
