"""Module demonstrating variable assignment and usage."""


GREETING = "Hello"  # String value - double quotes
GREETING_TWO = 'Hello World'  # String value - single quotes
ONE = 1  # Integer value

# Overwriting the value type of a variable from int to str
ONE = "One"

# Casting
TWO = int(2)
THREE = str(3)
FOUR = float(4)

print(GREETING)
print(ONE)
print(TWO)
print(THREE)
print(FOUR)

# Getting the type of a data
print(type(GREETING))
print(type(ONE))
print(type(TWO))
print(type(THREE))
print(type(FOUR))

# Legal variable names:
# ---------------------
# legalvar = "Legal"
# legal_var_1 = "Legal" => Snake case style
# _legal_var_2 = "Legal" => Snake case style
# LEGALVAR3 = "Legal" => Upper case style
# legalvar4 = "Legal"
# legalVar5 = "Legal" => Camel case style
# LegalVar6 = "Legal" => Pascal case style


# How to assign multiple variables
a, b, c = 1, 2, 3

# How to assign one value to multiple variables
ZERO = NONE = NULL = 0

print("The value of a is: ", a)
print("The value of b is: ", b)
print("The value of c is: ", c)
print("The value of ZERO is: ", ZERO)
print("The value of NONE is: ", NONE)
print("The value of NULL is: ", NULL)

# Unpacking: Python allows you to extract the values in a list or tuple into variables
fruits = ["apple", "banana", "cherry"]  # List
apple, banana, cherry = fruits
print("The value of apple is: ", apple)
print("The value of banana is: ", banana)
print("The value of cherry is: ", cherry)

colors = ("green", "yellow", "red")  # Tuple
(green, yellow, red) = colors
print("The value of green is: ", green)
print("The value of yellow is: ", yellow)
print("The value of red is: ", red)

# GLOBAL VARIABLES
# Global variables are accessible throughout the entire program. You can also
# make variable global by using the `global` keyword (global <variable_name>).
GLOBAL_VAR = "I am a global variable"


def access_global_var():
    """Function to access the global variable"""
    print(GLOBAL_VAR)


access_global_var()
