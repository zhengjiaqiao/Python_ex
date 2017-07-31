cars=100
# There are 100 cars available.
space_in_a_car=4
# Each car have 4 empty seats.
drivers = 30
# There are 30 drivers available today.
passengers = 90
# We have 90 passengers to transport.
cars_not_driven = cars - drivers
# 70 cars not have drevers,so they won't be driven.
cars_driven = drivers
# There are 30 cars available.
carpool_capacity = cars_driven * space_in_a_car
# We can transport 120 passengers. 
average_passengers_per_car = passengers / cars_driven
# Each car need transport 3 passengers.
print "There are",cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today"
print "We need to put about",average_passengers_per_car,"in each car."
