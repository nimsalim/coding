pets = [
    {"name": "Bella", "type": "Dog", "age": 3},
    {"name": "Milo", "type": "Cat", "age": 2},
    {"name": "Charlie", "type": "Parrot", "age": 1},
]

# Ask the staff to enter the pet number
pet_number = input("Enter the pet number (0-2): ")

try:
    # Try converting to an integer and accessing the list
    pet_index = int(pet_number)
    pet = pets[pet_index]
    print("Pet Details:")
    print("Name:", pet["name"])
    print("Type:", pet["type"])
    print("Age:", pet["age"])

except Exception as e:
    # Catch ANY error and print it out
    print("Oops! Something unexpected occurred!")
    print("Here's the error message:", e)  # This line prints the error message
    print(
        "This is the type of error", type(e)
    )  # This line prints the type of error that was caught
    print("Please try again.")


pets = [
    {"name": "Bella", "type": "Dog", "age": 3},
    {"name": "Milo", "type": "Cat", "age": 2},
    {"name": "Charlie", "type": "Parrot", "age": 1},
]

pet_number = input("Enter the pet number (0-2): ")

try:
    pet_index = int(pet_number)
    pet = pets[pet_index]
    print("Pet Details:")
    print("Name:", pet["name"])
    print("Type:", pet["type"])
    print("Age:", pet["age"])

# Handle this type of mistake FIRST
except ValueError:
    print("Please enter a **number** like 0, 1, or 2, not a word like 'Bella'.")

# Catch anything else not planned for
except Exception as e:
    print("Something unexpected occured!")
    print("Error message:", e)
    print("Type of error", type(e))
