conditions
temp = 70

if temp >= 65:
    print("Let's go for a walk!")
# if <condition>:
#   <execute block>
pet_age = 1

if pet_age < 2:
    print(
        "This pet needs extra playtime!"
    )  # Indented - this belongs to the if statement
    print(
        "Schedule two play sessions daily"
    )  # Indented - this also belongs to the if statement
print("Check food and water")  # Not indented - this happens regardless of age

# Indent after a colon: Statements like if, and others that you will learn about in later modules, end with a colon and require the next line(s) to be indented.
# Consistent indentation: Python standards recommend four spaces for indentation. Some developers prefer using Tab spaces, but it's important to never mix the two in your code.

num = 100
if num > 50:
    print("The number is greater than 50.")
    if num < 150:
        print("The number is also less than 150.")
        print("The number is between 50 and 150.")
    print("This line is part of the first if block.")
print("This line is outside both if blocks.")


num = input("Enter a number: ")
num = int(num)
if num > 10:
    print("The number is greater than 10.")
elif num == 10:
    print("The number is exactly 10.")

else:
    print("The number is less than 10.")


dog_age = 1
if dog_age > 2:
    print("The dog is an adult.")
elif dog_age < 2:
    print("The dog is a puppy.")


pet_health = input(
    "Enter the pet's health score out of 100: "
)  # health score out of 100
pet_health = int(pet_health)
if pet_health >= 90:
    status = "excellent"
elif pet_health >= 80:
    status = "good"
elif pet_health >= 70:
    status = "fair"
elif pet_health >= 60:
    status = "poor"
else:
    status = "Let's go the vet!"
print("The pet's health status is:", status)

# EXcercise
# Ask the user how many pets they currently own
current_pets = input("How many pets do you currently own? ")

# Convert the input to an integer
current_pets = int(current_pets)  # Convert to int

# Use conditional statements to determine eligibility for adoption
if current_pets > 5:
    print("You already have a lot of pets! You might not be eligible to adopt more.")
elif current_pets == 5:
    print("You already own 5 pets. Consider adopting later!")
elif current_pets == 0:
    print("You don't have any pets yet! Consider adopting your first pet.")
else:
    print("You have fewer than 5 pets. You're welcome to adopt more!")
