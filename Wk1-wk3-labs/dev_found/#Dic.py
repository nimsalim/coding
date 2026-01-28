# Dic
# Using separate variables for one dog
import enum


dog1Name = "Buddy"
dog1Age = 3
dog1Breed = "Golden Retriever"
dog1IsVaccinated = True

# To access information, you use each variable separately
print(f"Name: {dog1Name}")
print(f"Age: {dog1Age}")

# In Python, a dictionary is a container that holds data in pairs,
# made of a key and a value. It's similar to how a traditional dictionary pairs words (keys) with their definitions (values).
# Python uses dictionaries to organize information in a similar way.

dog = {"name": "Buddy", "age": 3, "breed": "Golden Retriever", "is_vaccinated": True}

Me = {
    "name": "Souleymane",
    "age": 30,
    "city": "New York",
    "is_student": True,
    "is_married": True,
}
print(Me["name"])

dog_supplies = {
    "leash": "leather",
    "food_bowl": "stainless steel",
    "kibble_amount": 2.5,
    "toy_count": 6,
    "bed_size": "large",
    "shampoo_brand": "PuppyClean",
    "vaccination_due_days": 30,
}

fish_tank = {
    "capacity_liters": 75,
    "fish_count": 12,
    "filter_type": "biological",
    "water_temperature": 24.5,
    "decoration": "coral reef",
    "lighting": "LED",
    "pH_level": 7.2,
}

cat_accessories = {
    "litter_box_type": "covered",
    "scratching_post_height_cm": 90,
    "food_brand": "WhiskerDelights",
    "treats_in_pack": 20,
    "collar_material": "nylon",
    "toy_type": "interactive",
    "grooming_frequency_days": 7,
}

pet = {}

pet["name"] = "Bella"
pet["age"] = 4
pet["species"] = "Cat"

print(pet)


pet = {
    "name": "Buddy",
    "age": 2,
    "breed": "Beagle"
}

# update pet information after adoption
pet["name"] = "Charlie"  # New family changed name
pet["age"] = 3  # After one year
pet["breed"] = "Beagle Mix"  # DNA test results

print(pet)

# Step 1: Create a dictionary with adoption details
pet = {
    "name": "Max",
    "age": 1,
    "species": "Dog"

}
# Step 2: Add a new key-value pair for adoption fee
# Use bracket notation to add adoption fee
pet["adoption_fee"] = 101.00

# Step 3: Update the pet's age
# Update the age to 2
pet["age"] = 3

# Step 4: Use an f-string to create a message for the adopter
# Add code to print a message with pet details
message = f"Congratulations on adopting {pet['name']}! They are a {pet['age']}-year-old {pet['species']} with an adoption fee of ${pet['adoption_fee']:.2f}."

# Step 5: Use a conditional to check the adoption fee
# Add a conditional to print a thank-you message or a different message
if pet["adoption_fee"] > 101:
    message += " Thank you for choosing to adopt a pet in need!"
else:   
    message += " We appreciate your interest in adopting!"  
print(message)

# Measure some strings:
words = ['Lion', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Fixes:
# - Corrected the for loop syntax to use 'in'
# - Used the built-in range() function instead of a tuple
# - Fixed indentation and usage of enumerate

# Original problematic code:
# range= (1, 10)
# for i range in []:
#    print(enumerate(range))

# Fixed code:
range_values = range(1, 10)
for i, value in enumerate(range(1, 10)):
    print(i, value)