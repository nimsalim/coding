class PetFood:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def show_info(self):
        print(f"{self.name} by {self.brand} - Price: ${self.price}")


class customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def buy_food(self, food):
        if food.price <= self.budget:
            print(f"Purchased {food.name} for ${food.price}")
        else:
            print(
                f"{self.name} cannot buy {food.name} because it costs ${food.price}, which exceeds their budget of ${self.budget}."
            )


food1 = PetFood("Chicken Delight", "Purina", 15)
food2 = PetFood("Salmon Feast", "Whiskas", 12)

customer1 = customer("Nimaga", 20)
customer2 = customer("Assetou", 10)

customer1.buy_food(food1)
customer1.buy_food(food2)
customer2.buy_food(food1)
