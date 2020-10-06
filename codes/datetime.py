from datetime import datetime

now = datetime.now()

print now.day
print now.month
print now.year
print now.second
print now.minute
print now.hour

print "Today's date is %02d/%02d/%04d" % (now.month, now.day, now.year)
print "The time is %02d:%02d:%02d" % (now.hour, now.minute, now.second)
print "The current date and time is %s" % (now)