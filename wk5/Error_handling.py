# List of pets
pets = [
    {"name": "Bella", "type": "Dog", "age": 3},
    {"name": "Milo", "type": "Cat", "age": 2},
    {"name": "Charlie", "type": "Parrot", "age": 1},
]

# Ask the staff to enter the pet number
pet_number = input("Enter the pet number (0-2): ")

# Convert input to an integer
pet_index = int(pet_number)

# Get the pet info
pet = pets[pet_index]
print("Pet Details:")
print("Name:", pet["name"])
print("Type:", pet["type"])
print("Age:", pet["age"])
