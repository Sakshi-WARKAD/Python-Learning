#--------------------------List in python-----------------------------------------------------------------------------------
# A built in data type that stores set of values. it can store elements of different type(Integer, float, string etc.)
# String - - immutable in python (Can't change)
# List -- mutable in python (change) 

list = ["Krishna", 12.45 , "Samiksha", 45, "Kamyar", "Haniya"]
print(list)

list[2] = "Roshi"
list[4] = "Raha"
print(list)

"""str = "Hello"
str[0] = "k"
                                              #It will through an error bcz strings are immutable in python.
print(str[0])
"""

list[0] = "Saras"
 
print(list[0])
print(list)

#---------------------------------------------------------------------------------------------
# List slicing

print(list[1:3])
print(list[:4])