# Create a list of pets, where each pet is represented as a dictionary with its details.
pets = [
    {
        "name": "Charlie",
        "species": "dog",
        "breed": "Golden Retriever",
        "age": 3,
        "weight": 55,
    },
    {"name": "Luna", "species": "cat", "breed": "Siamese", "age": 2, "weight": 10},
    {"name": "Max", "species": "dog", "breed": "Beagle", "age": 4, "weight": 30},
    {"name": "Bella", "species": "cat", "breed": "Maine Coon", "age": 5, "weight": 15},
]

# Open the following two files at the same time:
# - 'dogs.txt' will be used to write info about dogs
# - 'cats.txt' will be used to write info about cats

with open("dogs.txt", "w") as dogs_file, open("cats.txt", "w") as cats_file:
    # Iterate through the list of pets
    for pet in pets:
        # Create a formatted string with the pet's details
        sentence = f"{pet['name']} is a {pet['age']}-year-old {pet['breed']} that weighs {pet['weight']} pounds.\n"

        # Write to the appropriate file based on species
        if pet["species"] == "dog":
            dogs_file.write(sentence)
        elif pet["species"] == "cat":
            cats_file.write(sentence)
print(
    "Pet information has been written to dogs.txt and cats.txt."
)  # The code above creates two files, 'dogs.txt' and 'cats.txt', and writes the
