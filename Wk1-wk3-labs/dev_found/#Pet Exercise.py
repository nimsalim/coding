# Pet Exercise
# Use a for loop with range() to print numbers 1 through 3.
# To do 1: Add a for loop using range() here.

# Prompt the user to enter a pet's name.
# To do 2: Add a statement here to get the user input and assign it to the pet_name variable.

# Use a for loop to print each letter in the pet's name.
# To do 3: Add a for loop here to iterate over the pet_name string variable.

# Use len() to display the total number of letters in the pet's name.
# To do 4: Add a print statement here print the length of the pet_name variable.
for i in range(1, 4):
    print(i)
pet_name = input("Enter your pet's name: ")
for letter in pet_name:
    print(letter)
print(len(pet_name))


# Use a for loop with range() to print the numbers 1 through 3.
print("First three pets in the store:")

for pet_count in range(1, 4):
    print(f"Pet {pet_count}")

# Prompt the user to enter a pet's name.
pet_name = input("Enter a pet's name: ")

# Use a for loop to print each letter in the pet's name.
print("\nLetters in the pet's name:")

for letter in pet_name:
    print(letter)

# Use len() to display the total number of letters in the pet's name.
print(f"\nThe pet's name has {len(pet_name)} letters.")

# Using a while loop to assign an ID to 5 new pets in the store

# Initialize a variable to represent a pet ID.
pet_id = 1

print("New pet IDs:")

# While loop to print new pet IDs
while pet_id <= 5:  # Loop until pet_id is greater than 5.
    print(f"Pet {pet_id}")
    pet_id = pet_id + 1  # Increment the ID to avoid an infinite loop.


# Print the name of customers who make a purchase while the store is open.

# Initialize the loop condition variable to true.
store_is_open = True

# Start the loop and stop when the user enters "close".
while store_is_open:
    customer = input("Enter customer name (or 'close' to end the day): ")

    if customer == "close":
        store_is_open = (
            False  # Set the loop condition to false when the input is "close".
        )

    else:
        print(f"Processing order for {customer}")

