class PetFood:
    def __init__(self, food_name, food_type, food_price, food_description):
        self.food_name = food_name
        self.food_type = food_type
        self.food_price = food_price
        self.food_description = food_description

    def display_info(self):
        print(f"Food Name: {self.food_name}")
        print(f"Food Type: {self.food_type}")
        print(f"Food Price: ${self.food_price}")
        print(f"Food Description: {self.food_description}")


# Example usage:
food1 = PetFood("Kibble", "Dry", 25.99, "High-quality kibble for all breeds.")
food1.display_info()
