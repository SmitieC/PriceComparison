""" Component 3 of Price Checker Program
Ask user for their budget and also for unit of measure
Use already made functions to check that answers are valid
V1 is to ask for users budget
20/05/2022 Conor Smith"""


# float checker function
def float_check(question):
    while True:
        try:
            float_num = input(question)
            return float(float_num)

        except ValueError:
            print("please enter valid number\n")


budget = float_check("What is your budget?\n$")
