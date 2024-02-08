from datetime import datetime 

user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadLine = input_list[1]

deadLine_date = datetime.strptime(deadLine, "%d.%m.%Y")
today_date = datetime.today()

time_till = deadLine_date - today_date

hours_till = int(time_till.total_seconds() / 60 / 60 )


print(f"Dear user! Time remaining for your goal : {goal} is {hours_till} days ")

# print(datetime.datetime.strptime(deadLine, "%d.%m.%Y"))
# print(type(datetime.datetime.strptime(deadLine, "%d.%m.%Y")))

#we have 2 datetime. the first one is module. second one is module definition. this is also called which is class.

