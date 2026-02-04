#--------------------------List in python-----------------------------------------------------------------------------------
# A built in data type that stores set of values. it can store elements of different type(Integer, float, string etc.)
# String - - immutable in python (Can't change)
# List -- mutable in python (change) 

"""list = ["Krishna", 12.45 , "Samiksha", 45, "Kamyar", "Haniya"]
print(list)

list[2] = "Roshi"
list[4] = "Raha"
print(list)

"""
"""str = "Hello"
str[0] = "k"
                                              #It will through an error bcz strings are immutable in python.
print(str[0])
"""
"""
list[0] = "Saras"
 
print(list[0])
print(list)
"""
#---------------------------------------------------------------------------------------------
# List slicing
"""
print(list[1:3])
print(list[:4])
#------------------------------------------------------------
"""

List = ["Saras", "Bhakti", 23.4, "Delhi"]
print(List)

List.append(4)
print(List)

#-----Sort-----------

Numeric_list = [3,4,12,6]
Numeric_list.sort()
print(Numeric_list)

#------Reverse------------

Numeric_list = [3,4,12,6]
Numeric_list.reverse()
print(Numeric_list)

#-------------Sort in Descending order----------

Numeric_list = [3,4,12,6]
Numeric_list.sort(reverse=True)
print(Numeric_list)

#----------------pop--------------

Numeric_list = [3,4,12,6]
Numeric_list.pop(2)
print(Numeric_list)

#---------------Remove first occurance------------

Numeric_list = [3,4,12,6,4,17]
Numeric_list.remove(4)
print(Numeric_list)

#-------------insert element-----------------------------

Numeric_list = [3,4,12,6,4,17]
Numeric_list.insert(4,"Tanu")
print(Numeric_list)