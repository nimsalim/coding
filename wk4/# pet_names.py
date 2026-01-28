# Initialize the shelter pets dictionary.
# IDs that start with 'C' represent cats and
# those that start with 'D' represent dogs.
shelter_pets = {
    "D1": "Max",
    "D2": "Lucy",
    "D3": "Bailey",
    "D4": "Charlie",
    "C1": "Missy",
    "C2": "Felix",
}

# Print all pet names using dictionary values
print("\n--- All Pet Names ---")
for name in shelter_pets.values():
    print(name)

# Print all cat names using direct dictionary iteration
print("\n--- Cat Names Only ---")
for pet_id in shelter_pets:
    if pet_id[0] == "C":
        print(shelter_pets[pet_id])

# Print dog IDs and names using items()
print("\n--- Dog IDs and Names ---")
for pet_id, name in shelter_pets.items():
    if pet_id[0] == "D":
        print(f"Dog {pet_id}: {name}")

# Print the total number of pets in the shelter
print("\n--- Total pets in shelter ---")
print(len(shelter_pets))
