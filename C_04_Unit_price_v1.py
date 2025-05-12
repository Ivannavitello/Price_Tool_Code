# Functions goes here
def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        # uses 'strip' to remove whitespace before / after
        response = input(question).strip()

        if response != "":
            return response

        print("sorry, this can't be blank. Please try again./n")


def num_check(question, num_type="float", exit_code=None):
    """Checks that response is a float / integer more than zero"""

    if num_type == "float":
        error = "Please enter a number more than 0."
    else:
        error = "Please enter an integer more than 0."

    while True:

        response = input(question)

        # check for exit code return it if entered
        if response == exit_code:
            return response

        # check datatype is correct and that number
        # is more than zero
        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word  from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


print("")

# Main Routine goes here __1
print("Hello world")

# code that gets the unit price per Kg of an item that the user had enter calculate the cost and unit per kg.
# Fr example: user enter "Rice" as the item. They type	= "10000 grams"  or	"10 kg" then the user type the cost "$25.00"
# The unit price is then $2.50 per kg ( you need to make this code)

# Get item details
item = not_blank("Enter the name of the item: ")

# Get weight of the item
weight = input("Enter the weight (e.g., '10000 grams' or '10 kg'): ").strip().lower()

if "grams" in weight:
    weight_in_kg = float(weight.split()[0]) / 1000
elif "kg" in weight:
    weight_in_kg = float(weight.split()[0])
else:
    print("Invalid weight format. Please use 'grams' or 'kg'.")
    exit()

# Get cost of the item
cost = num_check("Enter the cost of the item in dollars (e.g., '25'): ")

# Calculate and display unit price
unit_price = float(cost) / weight_in_kg
print(f"The unit price of {item} is ${unit_price:.2f} per kg.")
# 
# 
# A smaller package of flour costs $1 for 1 kg, and a larger one costs $1.35 for 1.5 kg

