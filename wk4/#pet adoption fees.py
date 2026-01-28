# pet adoption fees
# initial adoption fee
# Initialize the dictionaries
size_to_fee = {"small": 125, "medium": 150, "large": 175, "extra large": 200}

shelter_pets = {
    "Buddy": "large",
    "Luna": "small",
    "Charlie": "medium",
    "Daisy": "extra large",
    "Stella": "unknown",
}

# Look up Buddy's size and fee using bracket notation
# To do 1: Add statements to print Buddy's size and fee

# Check if Luna exists and print her fee
# To do 2: Add if statement and print fee, if it exists

# Look up Daisy's fee with default values
# To do 3: Add statements using get() method

if "Buddy" in shelter_pets:
    buddy_size = shelter_pets["Buddy"]
    buddy_fee = size_to_fee[buddy_size]
    print(f"Buddy's size: {buddy_size}")
    print(f"Buddy's adoption fee: ${buddy_fee}")

if "Luna" in shelter_pets:
    luna_size = shelter_pets["Luna"]
    luna_fee = size_to_fee[luna_size]
    print(f"Luna's adoption fee: ${luna_fee}")

daisy_size = shelter_pets.get("Daisy", "Unknown size")
daisy_fee = size_to_fee.get(daisy_size, 100)
print(f"Daisy's adoption fee: ${daisy_fee}")


# Looping over the keys in a dictionary

print("Data recorded for a pet:")

pet_details = {"name": "Buddy", "age": 3, "type": "dog"}

for key in pet_details:  # By default, a dictionary returns its keys.
    print(key)

# Looping over the values in a dictionary

print("Values of the data recorded for the pet 'Buddy':")

pet_details = {"name": "Buddy", "age": 3, "type": "dog"}

for value in pet_details.values():  # Iterates over each value in the dictionary
    print(value)

# Looping over the keys and values in a dictionary

print("Keys and values for the pet 'Buddy':")

pet_details = {"name": "Buddy", "age": 3, "type": "dog"}

for (
    key,
    value,
) in pet_details.items():  # Iterates over each key and value in the dictionary
    print(f"{key}: {value}")
