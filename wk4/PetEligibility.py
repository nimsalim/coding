# Pet Eligibility
# Check whether the animal is old enough based on its species
def check_eligibility(pet):
    """Determine if a pet is old enough for spaying/neutering."""
    species = pet.get("species")
    age = pet.get("age_months")
    if (species == "cat" and age >= 5) or (species == "dog" and age >= 6):
        return True
    return False


# Determine the procedure name (spaying or neutering), based on the pet's sex
def get_procedure_name(sex):
    """Returns the appropriate procedure name based on pet's sex."""
    if sex == "female":
        return "spaying"
    else:
        return "neutering"


# Process each individual pet
def process_pet(pet_info):
    """Processes a single pet and prints if they are eligible for the procedure."""
    if check_eligibility(pet_info):
        procedure_name = get_procedure_name(pet_info.get("sex"))
        name = pet_info.get("name")
        print(f"{name} is ready for {procedure_name}")


# Start with a list of the un-sterilized pets in the shelter
pets = [
    {"name": "Whiskers", "age_months": 4, "sex": "female", "species": "cat"},
    {"name": "Mittens", "age_months": 6, "sex": "male", "species": "cat"},
    {"name": "Buddy", "age_months": 5, "sex": "male", "species": "dog"},
    {"name": "Luna", "age_months": 7, "sex": "female", "species": "dog"},
]

# Check each pet in the list
for pet in pets:
    process_pet(pet)
z
