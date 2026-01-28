# Log_operators
# Create two variables with number values
x = 5  # Assign the number 5 to variable x
y = 10  # Assign the number 10 to variable y

# Using the AND operator (both conditions must be true for the result to be true)
print(x < 10 and y > 5)  # This checks TWO things:
# 1. Is x less than 10? (5 < 10 is True)
# 2. Is y greater than 5? (10 > 5 is True)
# Since BOTH are True, the final result is True

# Using the OR operator (at least one condition must be true for the result to be true)
print(x > 10 or y > 5)  # This checks TWO things:
# 1. Is x greater than 10? (5 > 10 is False)
# 2. Is y greater than 5? (10 > 5 is True)
# Since at least ONE is True, the final result is True

# Using the NOT operator (reverses True to False, or False to True)
print(not (x > 10))  # This works in two steps:
# 1. First checks: Is x greater than 10? (5 > 10 is False)
# 2. Then reverses it: not(False) becomes True
# The final result is True
