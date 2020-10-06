cucumbers = 5
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber

print total_cost

print ">>>>>>>>>>>>>>>>>>>"

january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

september_to_december_rainfall = september_rainfall + october_rainfall + november_rainfall + december_rainfall

annual_rainfall += september_to_december_rainfall

print annual_rainfall

print "+++++++++++++++++++++"

cucumbers = 100
num_people = 6

# The quotient will be round down
whole_cucumbers_per_person = cucumbers / num_people

print whole_cucumbers_per_person

# The quotient will be a float
float_cucumbers_per_person = float(cucumbers) / num_people

print float_cucumbers_per_person