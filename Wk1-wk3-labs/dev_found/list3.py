#promote the pets
pets = ["Buddy", "Mittens", "Goldie", "Spike", "Bella"]
for i in range(len(pets)):
    pets[i] = f"{pets[i]} - On Sale!"
    print("Promoted Pet List:", pets)

# creating and iterating over a list of dictionaries
# Define a list of dictionaries, each representing a pet.
pets = [
    {
        "name": "Buddy",
        "type": "Dog", 
        "age": 3
    },
    {
        "name": "Mittens",
        "type": "Cat",
        "age": 5
    },
    {
        "name": "Goldie", 
        "type": "Fish",
        "age": 2
    },
]

# Loop through the list of dictionaries.
for pet in pets:
    # Access and print the values in each dictionary.
    print(
        f"Name: {pet['name']}, "
        f"Type: {pet['type']}, "
        f"Age: {pet['age']} years"
    )

# Create a list of dictionaries representing pets.
pets = [
    {"name": "Buddy", "type": "Dog", "age": 3},
    {"name": "Mittens", "type": "Cat", "age": 5},
    {"name": "Goldie", "type": "Fish", "age": 2},
]

# Use a direct iteration for loop to iterate over the list of dictionaries.
# To do 1: Add a direct iteration for loop header to iterate over the pets list.
    # To do 2: Print the pet details using f-strings.
 
    # To do 3: Add a conditional to check if the pet's age is 2 or less, and print a young pet message if it's true.

for pet in pets:
    print(
        f"Name: {pet['name']}, "
        f"Type: {pet['type']}, "
        f"Age: {pet['age']} years"
    )
    if pet['age'] <= 2:
        print(f"{pet['name']} is a young pet!")
# i need to add a new key value pair to the dictionaries called adoption priority   
for pet in pets:
    if pet['age'] > 2:
        pet['adoption_priority'] = 'High'
    else:
        pet['adoption_priority'] = 'Normal'
print(pets)


last_pet= pets.pop()
print("Last pet removed:", last_pet)

Readded_pet= pets.append(last_pet)
print("Readded pet:", last_pet)

print("Updated pets list:", pets)

pets.append("Spike")
print("Final pets list:", pets)

inserted_pet= pets.insert(1,  {"name": "Daisy", "type": "Fish", "age": 2})
print("Inserted pet at index 1:", pets)

print("Original pet list:", pets)

print("Inserting Fluffy at index 2")
pets.insert(2, "Fluffy")
print("After insertion:", pets)

pets.pop(3)
print("After removing pet at index 3:", pets)
pets.pop(2)
print("After removing pet at index 2:", pets)



# Create a list of pet names that represents the pet inventory.
pets = ["Buddy", "Goldie", "Spike"]

# Print the original list of pets.
print("Original list of pets:", pets)

# Define a list of updates whose elements are dictionaries of actions.
updates = [
    {"action": "add", "name": "Mittens"},
    {"action": "adopt", "name": "Goldie"},
    {"action": "promote", "name": "Bella"},
]

# Loop through the updates list and apply each action to the pet inventory.
for update in updates:
    if update["action"] == "add":
        # Add the pet only if it is not already in the list.
        if update["name"] not in pets:
            pets.append(update["name"])
            print(f"Added {update['name']} to the list.")
    elif update["action"] == "adopt":
        # Remove the pet if it is in the list.
        if update["name"] in pets:
            pets.remove(update["name"])
            print(f"{update['name']} has been adopted and removed from the list.")
    elif update["action"] == "promote":
        # Insert the pet at index 0.
        if update["name"] not in pets:
            pets.insert(0, update["name"])
            print(f"Promoted {update['name']} to the first position in the list.")

# Print the final list of pets.
print("Final list of pets:", pets)

pets.pop(1) 
print("After removing pet at index 1:", pets)
