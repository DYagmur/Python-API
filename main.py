calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(number_of_days):    
        return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}"
    

def validate_and_execute():
    try:
        user_input_number  = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0 . Please enter a valid positive number")
        else :
            print("You entered negative number. Please  enter a valid positive number.")
    except  ValueError:
        print ("Invalid input. Please enter a numeric value.")
        
user_input = "" #assign an empty string to user_input
while user_input != "exit":  #condition gets evaluated
    user_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
    for num_of_days_element in user_input.split():
        validate_and_execute()  #user is prompted for its input
#function is called and input is validated and executed
#second loop : check if exiit was typed in


#conditional notes
#
# if condition is correct:
    #then do this
#otherwise:
#do that ##### contition can be tue or false.
#boolen data type have  two values True or False.


#list --> [10, 20, 30, 40] 