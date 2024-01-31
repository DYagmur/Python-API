calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(number_of_days):    
        return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}"
    

def validate_and_execute():
    try:
        user_input_number  = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0 . Please enter a valid positive number")
        else :
            print("You entered negative number. Please  enter a valid positive number.")
    except  ValueError:
        print ("Invalid input. Please enter a numeric value.")
    
while True:  
    user_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
    validate_and_execute()



#conditional notes
#
# if condition is correct:
    #then do this
#otherwise:
#do that ##### contition can be tue or false.
#boolen data type have  two values True or False.