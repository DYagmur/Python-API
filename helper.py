
def days_to_units(number_of_days, convertion_unit):    
    if convertion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} hours"
    elif convertion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} minutes"
    else:
        return "Invalid unit for conversion. Please use 'hours' or 'minutes'"

def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number  = int(days_and_unit_dictionary["days"])            #items can be accessed by its key name. you can use square brackets or get() method your_dict["days"] OR your_dict.get("days")
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"] )
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0 . Please enter a valid positive number")
        else :
            print("You entered negative number. Please  enter a valid positive number.")
    except  ValueError:
        print ("Invalid input. Please enter a numeric value.")
    
    
user_input_message = ("hey user, enter number of days and conversation unit!\n")


