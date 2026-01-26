# Loops
# adding new pets to the inventory without loops
print("Generating new pet processing messages")


# Add the first pet.
pet_name = input("Enter pet name 1: ")
print(f"Welcome to the pet store, {pet_name}!")
print(f"{pet_name}, we will take good care of you.")
print(f"Added {pet_name} to the inventory.")
print("---------------------------------------")

# Add the second pet.
pet_name = input("Enter pet name 2: ")
print(f"Welcome to the pet store, {pet_name}!")
print(f"{pet_name}, we will take good care of you.")
print(f"Added {pet_name} to the inventory.")
print("---------------------------------------")

# Add the third pet.
pet_name = input("Enter pet name 3: ")
print(f"Welcome to the pet store, {pet_name}!")
print(f"{pet_name}, we will take good care of you.")
print(f"Added {pet_name} to the inventory.")
print("---------------------------------------")

# adding pet names using loops
number_of_pets = 3
for i in range(number_of_pets):
    pet_name = input(f"Enter pet name {i + 1}: ")
    print(f"Welcome to the pet store, {pet_name}!")
    print(f"{pet_name}, we will take good care of you.")
    print(f"Added {pet_name} to the inventory.")
    print("---------------------------------------")

numbers=[1, 2, 3, 4, 5]
for number in numbers:
    print(f"Number: {number}")

for pet_count in range(1, 6, 1):  # Loops from 1 to 5
    print(f"Pet {pet_count}")

# Looping over a string to display pet name characters

pet_name = "Tepsy"
print("\nLetters in the pet's name:")

for letter in pet_name:  # Iterates over each character in the string
    print(letter)