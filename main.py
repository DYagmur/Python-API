# calculation_to_units = 24
# name_of_unit = "hours"


def days_to_units(number_of_days, convertion_unit):    
    if convertion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} hours"
    elif convertion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} minutes"
    else:
        return "Invalid unit for conversion. Please use 'hours' or 'minutes'"

def validate_and_execute():
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
        
user_input = "" #assign an empty string to user_input
while user_input != "exit":  #condition gets evaluated
    user_input = input("Hey user, enter a number of days and conversation unit\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()
    

 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#      user_input = input("Hey user, enter a number of days and conversation unit\n")
#     list_of_days = user_input.split(", ")
#     print(list_of_days)
#     print(type(list_of_days))
#     print(set(list_of_days))
#     print(type(set(list_of_days)))
#     for num_of_days_element in list_of_days:
#         validate_and_execute()   #user is prompted for its input
        
        
#function is called and input is validated and executed
#second loop : check if exiit was typed in


#conditional notes
#
# if condition is correct:
    #then do this
#otherwise:
#do that ##### contition can be tue or false.
#boolen data type have  two values True or False.

# print("some text") #prints to the standard output device
# input("enter value") #asks user for input
# set([1, 3, 4]) #returns a new set
# int("20") # converts a value object into integer

# "2, 3".split()
# [1, 3, 4].count()



