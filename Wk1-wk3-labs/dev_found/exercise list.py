#list exercises

# Create a list of pet names.
#   To do 1: Create a list called pets with at least 5 pet names.
pets = ["Buddy", "Mittens", "Goldie", "Spike", "Bella"]

print("Pet list:")

# Loop forward through the list using range() and print the names with an even index in uppercase.
#   To do 2: Add a loop to print pets in forward order with uppercase for even indices.
for i in range(0, len(pets), 1):                    # Forward loop
    if i % 2 == 0:                                  # Check if the index is even.
        print(f"Pet {i + 1}: {pets[i].upper()}")    # Print in uppercase if index is even.
    else:
        print(f"Pet {i + 1}: {pets[i]}")            # Print normally if index is odd.

print("\nPet list in reverse order:")

# Loop backward through the list using range().
#   To do 3: Add a loop to print pets in backward order.
for i in range(len(pets) - 1, -1, -1):          # Backward loop
    print(f"Pet {len(pets) - i}: {pets[i]}")    # Print pet names in reverse order.



# Define a list of pet names.
pets = ["Buddy", "Mittens", "Goldie", "Spike", "Bella"]

print("Original Pet List:", pets)   # Print the original pet list.

# Use a counting loop to modify the names of pets and indicate they have been sold.
for i in range(len(pets)):      # Loop through all of the indices of the list.
    pets[i] = pets[i].lower()   # Change the pet name to lowercase.

print("Updated Pet List:", pets)    # Display the modified list.