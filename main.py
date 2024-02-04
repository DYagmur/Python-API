from helper import validate_and_execute, user_input_message

import os
import logging

logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")
print(os.name)

#for this example is  imported directly, but in your code you should use `from helper import *` or specific functions.


user_input = "" #assign an empty string to user_input
while user_input != "exit":  #condition gets evaluated
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute(days_and_unit_dictionary)
    
    
    
############# DATA TYPES ################   
        
    
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



