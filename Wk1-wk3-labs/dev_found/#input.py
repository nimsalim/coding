# input
# Prompt user for input
pet_name = input("Enter your pet's name: ")
owner_name = input("Enter the owner's name: ")

# Calculate the lengths of both names
length_pet_name = len(pet_name)
length_owner_name = len(owner_name)

# Compare the lengths and print results
print(
    "Is the pet's name longer than the owner's name?",
    length_pet_name > length_owner_name,
)
print(
    "Are the pet's name and owner's name the same length?",
    length_pet_name == length_owner_name,
)

# Prompt user for the number of pets and maximum capacity
pets_in_store = input("Enter the number of pets in the store: ")
max_capacity = input("Enter the store's maximum capacity: ")

# Convert inputs to integers
pets_in_store = int(pets_in_store)
max_capacity = int(max_capacity)

# Compare pets in store to maximum capacity
print("Is the store over capacity?", pets_in_store > max_capacity)
print("Is the store under capacity?", pets_in_store < max_capacity)
