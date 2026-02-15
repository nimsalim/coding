class PetFood:
    def __init__(
        self, food_name, food_type, food_price, food_quantity, food_description
    ):
        self.food_name = food_name
        self.food_type = food_type
        self.food_price = food_price
        self.food_quantity = food_quantity
        self.food_description = food_description

    def display_info(self):
        print(f"Food Name: {self.food_name}")
        print(f"Food Type: {self.food_type}")
        print(f"Food Price: ${self.food_price}")
        print(f"Food Quantity: {self.food_quantity}")
        print(f"Food Description: {self.food_description}")

    def update_quantity(self, new_quantity):
        self.food_quantity += new_quantity
        print(f"Updated quantity: {self.food_quantity} units available.")

    def apply_discount(self, discount_percentage):
        discount_amount = self.food_price * (discount_percentage / 100)
        self.food_price -= discount_amount
        print(
            f"Discount applied: {discount_percentage}%. New price: ${self.food_price:.2f}"
        )

    def purchase_food(self, quantity):
        if quantity > self.food_quantity:
            print("Sorry, not enough stock available.")
        else:
            self.food_quantity -= quantity
            total_cost = quantity * self.food_price
            print(f"Purchased {quantity} units for a total of ${total_cost:.2f}.")


# Example usage:
food1 = PetFood("Kibble", "Dry", 25.99, 45, "High-quality kibble for all breeds.")
food1.display_info()
food1.apply_discount(50)
food2 = PetFood("Canned Tuna", "Wet", 35.99, 30, "Delicious canned tuna for cats.")
food2.display_info()
food2.apply_discount(10)
food2.apply_discount(25)
food1.update_quantity(60)
food1.display_info()

food3 = PetFood("salmon", "wet", 15.99, 20, "salmon for cats")
food3.display_info()
food3.apply_discount(20)
food3.update_quantity(10)

food1.purchase_food(10)
food1.display_info()
food2.purchase_food(5)
food2.display_info()
