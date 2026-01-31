# Returns
"""
Module demonstrating return values and return statements in Python functions.
This module illustrates:
- Functions that return computed values
- Capturing return values in variables
- Functions with no explicit return statement (implicitly return None)
- Functions with explicit return None
- Evaluating expressions directly in return statements
Key concepts:
- Return statements send values back to the caller
- Functions without return statements or with only 'return' return None
- Return values can be captured and used in subsequent operations
- Expressions can be evaluated and returned in a single statement
"""


def add_numbers(a, b):
    """Adds the two numbers together and returns the result"""
    result = a + b
    return result


# The sum_result variable stores the return value from the add_numbers function call
sum_result = add_numbers(5, 3)

# Prints: 8
print(sum_result)


# Function with no return statement
def greet(name):
    print(f"Hello, {name}")


# Function explicitly returning None
def greet_return_none(name):
    print(f"Hello, {name}")
    return None


result1 = greet("Anita")  # result1 is None
result2 = greet_return_none("Sam")  # result2 is None


def calculate_food_needed(num_dogs, num_cats):
    """Calculate daily food needed in pounds"""
    return (num_dogs * 2) + (num_cats * 1.5)


daily_food = calculate_food_needed(5, 3)
# Prints: 14.5
print(daily_food)

def assess_adoption_eligibility(home_visit_score, references_check):
    """Assess if a potential adopter is ready"""
    print("Evaluating adoption readiness...")
    print("Checking home visit score...")
    return home_visit_score > 7
    print("Did not pass home check, checking additional criteria...")  # This line never executes
    return references_check  # This line never executes

is_ready = assess_adoption_eligibility(8, True)
# Prints: Evaluating adoption readiness...
# Prints: Checking home visit score...
# is_ready will be True

print(is_ready)
# Prints: True

#In this example, the function assess_adoption_readiness checks if a potential adopter is eligible to adopt a pet. It does this by checking if the two parameters meet the criteria defined in the function. The first return statement returns the value from evaluating the expression home_visit_score > 7. It will return either True or False, depending on the value of the home_visit_score variable. However it will not proceed to the next statement for any reason -- once the function reaches a return statement, it exits the function no matter what.
#Instead, you can use multiple return statements inside different if-else statements. Here's how to properly implement the assess_adoption_readiness function.
def assess_adoption_eligibility(home_visit_score, references_check):
    """Assess if a potential adopter is eligible"""
    print("Evaluating adoption readiness...")
    
    if home_visit_score > 7:
        print("Adopter meets criteria based on their home visit score")
        return True
    elif references_check:
        print("Adopter meets criteria based on their references")
        return True
    else:
        print("Adopter does not meet any criteria for adoption")
        return False

is_ready = assess_adoption_eligibility(8, False)
# Prints: Evaluating adoption readiness...
# Prints: Adopter meets criteria based on their references
# is_ready will be True

print(is_ready)
# Prints: True
