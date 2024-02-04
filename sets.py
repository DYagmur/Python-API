#another built-in data type of python

#as with lists, used to store multiple items of data.

#does not allow duplicate values

my_set = {"January"  , "February", "March"}
for element in my_set:
    print(element)
    
    
my_set.add("April")

print(my_set)

my_set.remove("February")
print(my_set)