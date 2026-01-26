#Pets
# Create a list of pet names.
# To do 1: Create a list called pets with at least 5 pet names.

# Use a direct iteration for loop to iterate over the list and categorize the pet names.
# To do 2: Add a for loop header that iterates over the pets list.
    # To do 3: Add a conditional to check the length of the pet name.
    #          If the pet name has more than 5 characters, print the name with a "(Long)" label.
    #          Otherwise, print the name with a "(Short)" label.

pets = ['Buddy', 'Maximilian', 'Luna', 'Charlie', 'Daisy']
for pet in pets:
    if len(pet) > 5:                                                                                                                                                                                             ) > 5:
        print(f"{pet} (Long)")
    else:
        print(f"{pet} (Short)")

# Define a list of pet names.
pets = ["Buddy", "Mittens", "Goldie", "Spike", "Bella"]

# Loop forward through the list using range().
for i in range(0, len(pets), 1):  # Start at 0, stop at the length of the list, step by 1.
    print(f"Pet {i + 1}: {pets[i]}")

# Define a list of pet names.
pets = ["Buddy", "Mittens", "Goldie", "Spike", "Bella"]

# Loop backward through the list using range().
for i in range(len(pets) - 1, -1, -1):  # Start at the last index, stop before -1, step by -1.
    print(f"Pet {len(pets) - i}: {pets[i]}")

