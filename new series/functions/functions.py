calculation_days_to_hour = 24
name_of_hour = "hours"


def days_of_units(no_of_days):
    return f" in {no_of_days} days we have {no_of_days * calculation_days_to_hour} hours"
    


def validate_values_of_days():
    
    if user_input.isdigit():
        user_input_no = int(user_input)
        if user_input_no > 0:
            calulated_value = days_of_units(user_input_no)
            print(calulated_value)
        elif user_input_no == 0:
            print("you cant have  0 to calculate")
    else:
        print("invalid input only positive numbers needed")


user_input = input("hey enter a number of days you will like to know the hour \n")
validate_values_of_days()