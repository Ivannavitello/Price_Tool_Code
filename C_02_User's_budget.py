def num_check(question, num_type="float", low=None, high=None, exit_code=None, ):
    """Checks that response is a float / integer more than zero"""

    global error
    if num_type == "float":
        error = "Please enter a number more than 0."
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

            if response > 1:
                print("response is more than one, returning it")
            else:
                print(error)

            if response > 99999999:
                print("Response is too high!")
                print(error)
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# def user_budget(question, valid_ans):

# Main Routine goes here

budget = num_check("What is your budget? $")

# Output error message/ success message
if budget < 1:
    print(f"{budget} is too young")
elif budget > 99999999:
    print(f"{budget} is too old")
else:
    print(f"{budget} bough a ticket ")

print(f"your budget is ${budget}")

# A COde that ask users how many items they need to compare,
# them the users will list

Users_v1 = number
