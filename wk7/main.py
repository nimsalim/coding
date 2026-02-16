if choice == "1":
    name = input("Enter pet name: ")
    species = input("Enter pet species (dog/cat/other): ")
    age = input("Enter pet age: ")
    color = input("Enter pet color: ")  # Add input for color
    pet_manager.add_pet(name, species, age, color)  # Add color property
