import datetime

#Taking input from the user
birthdate = input("Enter your Date of birth in the format YYYY-MM-DD: ")

#Converting the string to DateTime format
birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d")

# Getting the current date
currentdate = datetime.datetime.now()

# Calculating the age
age = currentdate.year - birthdate.year

# Displaying the current date
print("Today's date:", currentdate.strftime("%Y-%m-%d"))

# Printing the age
print("Your age is:", age, "years")

# Checking if the user's birthday has passed in the current year
if currentdate.month < birthdate.month:
    age = age - 1

# Calculating the number of months
months = currentdate.month - birthdate.month

# Printing the age in years and months
print("Your age is:", age, "years and", months, "months")