# assign a value to the variable cars
cars = 100
# assign a value to the variable space_in_a_car
space_in_a_car = 4.0
# assign a value to the variable drivers
drivers = 30
# assign a value to the variable passengers
passengers = 90
# assign a value to the variable cars_not_driven
cars_not_driven = cars - drivers
# assign a value to the variable cars_driven
cars_driven = drivers
# assign a value to the variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# assign a value to the variable average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

# prints the two strings and the variable cars
print "There are", cars, "cars available."
# prints the two strings and the variable drivers
print "There are only", drivers, "drivers available."
# prints the two strings and the variable cars_not_driven
print "There will be", cars_not_driven, "empty cars today."
# prints the two strings and the variable carpool_capacity
print "We can transport", carpool_capacity, "people today."
# prints the two strings and the variable passengers
print "We have", passengers, "to carpool today."
# prints the two strings and the variable average_passengers_per_car
print "We need to put about", average_passengers_per_car, "in each car."
