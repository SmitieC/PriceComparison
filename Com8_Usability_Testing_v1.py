""" Component 8 of Price Checker Program
Fix minor errors in the program found through usability testing
V1 is to fix first set of errors
4/06/2022 Conor Smith"""


# float checker function
# cannot allow negative numbers
def float_check(question):
    while True:
        try:
            float_num = input(question)
            if float(float_num) < 0:
                print("please enter a positive number")
                # Create second loop to only allow positive numbers
            else:
                return float(float_num)
        except ValueError:
            print("please enter valid number:\n")


# Function to check for blank entries
# it also must allow spaces in the middle of an entry
def not_blank(question):
    valid = ""
    # using .isalpha check for response
    while not valid.isalpha():
        valid = input(question)
        if valid == "" or valid[0].isalpha() != True:
            # changed to only query first position
            print("This cannot be blank...")
        else:
            return valid


name = not_blank("What is the name of the item?\n")
