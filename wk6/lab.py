# Step 1: Define the PetFood class with the __init__ constructor
class PetFood:
    def __init__(self, name, brand, animal_type, price, weight):
        self.name = name
        self.brand = brand
        self.animal_type = animal_type
        self.price = price
        self.weight = weight


# Step 2: Create three instances of PetFood
food1 = PetFood("Chicken Delight", "Purina", "Dog", 15, 5)
food2 = PetFood("Salmon Feast", "Whiskas", "Cat", 12, 3)
food3 = PetFood("Veggie Bites", "Oxbow", "Rabbit", 10, 2)

# Step 3: Print attributes of each instance
print(
    f"Food 1: {food1.name}, Brand: {food1.brand}, Type: {food1.animal_type}, Price: ${food1.price}, Weight: {food1.weight} lbs"
)
print(
    f"Food 2: {food2.name}, Brand: {food2.brand}, Type: {food2.animal_type}, Price: ${food2.price}, Weight: {food2.weight} lbs"
)
print(
    f"Food 3: {food3.name}, Brand: {food3.brand}, Type: {food3.animal_type}, Price: ${food3.price}, Weight: {food3.weight} lbs"
)
