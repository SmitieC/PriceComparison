""" Component 1 of Price Checker Program
Set out Lists Variables and functions to then build on in future components
V2 is making a function to test for digit inputs
Trial 3 is to continue development on trial 1's number checker to allow floats
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


# float checker function
def float_check(question):
    while True:
        try:
            float_num = input(question)
            return float(float_num)

        except ValueError:
            print("please enter valid number:\n")


# Main Routine
# removed blank checker main routine as it was not required for v2 testing
# name = not_blank("What is your name: ")
# using print statement to test the function
# print(f"Hello {name}!")
number = float_check("What is your budget?\n$ ")
print(number)
