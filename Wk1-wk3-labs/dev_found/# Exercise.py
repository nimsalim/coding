# Exercise
# and operator
dog_age = 8  # Choose a number
dog_weight = 6  # Choose a number
print(dog_age > 2 and dog_weight > 20)  # Is the dog an adult and over 20 pounds?

# or operator
store_day = "Saturday"  # Choose: "Saturday" or "Sunday"
adoption_event = True  # Choose: True or False
print(store_day == "Saturday" or adoption_event)  # Is it Saturday or an adoption event?

# not operator
store_closed = False  # Choose: True or False
print(not store_closed)  # Is the store open?

# Combining logical operators
has_collar = False
is_microchipped = True
print((dog_age >= 1) and (has_collar or is_microchipped))  # Is the dog adoptable?

input_age = 5  # Choose a number
input_weight = 15  # Choose a number
print((input_age < 10) or (input_weight > 20))  # Is the dog young or heavy?
