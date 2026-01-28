#Add Pets
# To do 1: Create a variable named store_accepting_pets to track if more pets need to be added

# To do 2: Create a variable to keep count of how many pets have been added

# Use a while loop to add new pets to the store
# To do 3: Add a while loop statement header that continues while store_accepting_pets is True
    # To do 4: Ask the user to input a pet type (or 'done' to finish)
    # To do 5: Check if the user wants to stop adding pets
    # To do 6: If not done, print a message confirming the pet was added and increment the counter

# To do 7: Print a message showing how many pets were added to the inventory

store_accepting_pets = True
pets_added_count = 0

while store_accepting_pets:
    pet_type = input("Enter a pet type (or 'done' to finish): ")
    if pet_type == "done":
        store_accepting_pets = False
    else:
        print(f"Added {pet_type} to the store.")
        pets_added_count += 1

print(f"Added {pets_added_count} pets to the inventory.")