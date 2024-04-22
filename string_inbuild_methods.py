# IN BUILD METHODS OF STRINGS IN PYTHON
# FORMAT METHOD
name = "John"
age = 30
result = "My name is {} and I am {} years old".format(name, age)

# Using f-strings for string interpolation
name = "John"
age = 30
result = f"My name is {name} and I am {age} years old" 

# Extracting a substring using slicing
string = "Hello World"
result = string[6:]
#for lower case
string = "Hello World"
result = string.lower()
#for upper case
string = "Hello World"
result = string.upper()
# to replace a string
string = "Hello World"
result = string.replace("Hello", "Hi")
#occerance of sub strings
string = "Hello World"
count = string.count("l")
#whether it starts with the particular string
string = "Hello World"
starts_with = string.startswith("Hello")
#ending
string = "Hello World"
ends_with = string.endswith("World")
#finding a string
string = "Hello World"
index = string.find("World")

