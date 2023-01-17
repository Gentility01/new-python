# calculate no of hour in days
hour_in_a_day = 24


def no_of_days_in_hours(days):
    if days == 1:
        return f"{days} day have {days * hour_in_a_day} hours in it"
    else:
        return f"{days} days have {days * hour_in_a_day} hours in it"


user_input = input("enter the number of days you want to convert to hours \n")


def validate_and_envaluate_user_input():
    try:
        user_input.isdigit()
        convert_user_input = int(user_input)
        if convert_user_input == 0 or convert_user_input < 0:
            print("invalid number")
        else:
            print(no_of_days_in_hours(convert_user_input))
    except:
        print("only integers needed")


validate_and_envaluate_user_input()

