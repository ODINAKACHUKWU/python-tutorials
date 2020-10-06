age = 13
print "I am " + str(age) + " years old!"

print ">>>>>>>>>>>>>>>>>>>"

number1 = "100"
number2 = "10"

string_addition = number1 + number2 

int_addition = int(number1) + int(number2)

print string_addition
print int_addition

string_num = "7.5"

print float(string_num)

print "========================="

skill_completed = "Python Syntax"
exercises_completed = 13

#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100

point_total += exercises_completed * points_per_exercise

print "I got " + str(point_total) + " points!"