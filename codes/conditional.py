if 25 > 20:
    print "This is correct!"
else:
    print "This is wrong!"
    
if 20 == 30:
    print "This is correct!"
else:
    print "This is wrong!"
    
def greater_less_or_equal_5(number):
    if number > 5:
        print "The number is greater than 5!"
    elif number < 5:
        print "The number is less than 5!"
    else:
        print "The number is equal to 5!"
        
greater_less_or_equal_5(10)
greater_less_or_equal_5(3)
greater_less_or_equal_5(5)

print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

# Grade converter

def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "C"
    elif grade >= 65 and grade <= 69:
        return "D"
    else:
        return "F"
      
# This should print an "A"
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)