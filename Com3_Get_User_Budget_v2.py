""" Component 3 of Price Checker Program
Ask user for their budget and also for unit of measure
Make a function to check that answers are valid
V2 is to ask for users unit of measure
20/05/2022 Conor Smith"""


# Function to check for unit of measure
def unit_check(question):
    error = "\nSorry, you must enter a valid unit of measure\n"
    unit = ""
    while unit != "l" and unit != "ml" and unit != "g" and unit != "kg":
        unit = input(question).lower()
        if unit == "ml" or unit == "l" or unit == "g" or unit == "kg":
            return unit
        else:
            print(error)


unit_of_measure = unit_check("what is your unit of measure\nl, ml, g, kg:")
