class Pet:
    name = ""
    species = ""
    age = 0
    price = 0


# Use the Pet class to create create 1 new instance of a Pet
pet1 = Pet()


# Assigning values to pet1 object's attributes name, species, age, and price
pet1.name = "Fluffy"
pet1.species = "Cat"
pet1.age = 3
pet1.price = 500

print("-----Printing pet1 object attributes after assigning values-----")
# use f string to print the attributes
print(f"Pet 1 Name: {pet1.name}")  # Output: ""
print(f"Pet 1 Species: {pet1.species}")  # Output: "Cat"
print(f"Pet 1 Age: {pet1.age}")  # Output: 3
print(f"Pet 1 Price: {pet1.price}")  # Output: 500


pet2 = Pet()
pet2.name = "Tepsy"
pet2.species = "cat"
pet2.age = 5
pet2.price = 1000
print("-----Printing pet2 object attributes after assigning values-----")
print(f"{pet2.name} is a {pet2.age} year old {pet2.species} that costs ${pet2.price}")
