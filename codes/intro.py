from __future__ import print_function
import keyword

print ('This is the list of Python keywords:')
print (keyword.kwlist)

int_num = 3
person = "John"
true = True
float_num = 2.31
null = None

print (">>>>>>>>>>>>>>>>>>>")

print (type(int_num))
print (type(person))
print (type(true))
print (type(float_num))
print (type(null))

print (">>>>>>>>>>>>>>>>>>>")

print (int_num)
print (person)
print (true)
print (float_num)
print (null)

print ("+++++++++++++++++++++")

# Multi-line string:
haiku = """The old pond,
A frog jumps in:
Plop!
"""

# The code below will work only in python 2
# >>> print 'Hello, world!'
