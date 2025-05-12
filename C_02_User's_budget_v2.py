def int_check(question):
    """Checks users enter an integer"""

    error = "Please enter an integer."

    while True:

        try:
            # Return the response if it" an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# Main Routine goes here

# loop for testing purposes....
while True:

    print()

    # ask user for their name
    # replace with call to 'not blank' function!

    # Aks for their age check it's between 12 and 120
    budget = int_check("What is your budget?: ")

    # Output error message/ success message
    if budget < 1:
        print(f" Please enter a budget more than $0")
        continue
    elif budget > 9999999999999:
        print(f"Response is too high!")
        continue
    else:
        print(f"your budget is ${budget}")
        break


# A code that ask the users for the item,
# the unit of that product
# and also the cost of it per Unit

print("")
print("GoodBye!")