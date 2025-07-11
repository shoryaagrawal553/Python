# in python by default all the user input values are of string type
# so we need to convert them to the required type

age= input("Enter your age ")

# new_age= age +5  # TypeError: can only concatenate str (not "int") to str20

# to convert the string to integer we can use int() function
new_age= int(age)+5
print(new_age)

# other such functions are: float(), str(), bool()
print(float(new_age)) # converts to float

