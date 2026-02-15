# Define a PetFood class to manage pet food inventory and pricing
class PetFood:
    """Represents a pet food product with inventory and pricing management."""

    def __init__(self, name, brand, price, quantity):
        """
        Initialize a PetFood instance.

        Args:
            name (str): The name of the pet food product.
            brand (str): The brand/manufacturer of the pet food.
            price (float): The current price of the product per unit.
            quantity (int): The current stock quantity available.
        """
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity

    def show_info(self):
        """Display the product details: name, brand, price, and stock quantity."""
        print(
            f"{self.name} by {self.brand} - Price: ${self.price} - Stock: {self.quantity} units"
        )

    def apply_discount(self, discount_percentage):
        """
        Calculate and display the new price after applying a discount.

        Note: This method prints the discounted price but does not modify self.price.

        Args:
            discount_percentage (float): The discount amount as a percentage (e.g., 20 for 20% off).
        """
        # Calculate the discount amount in dollars
        discount_amount = self.price * (discount_percentage / 100)
        # Calculate the new price after subtracting the discount
        new_price = self.price - discount_amount
        print(
            f"After a {discount_percentage}% discount, the new price of {self.name} is: ${new_price:.2f}"
        )

    def update_stock(self, amount_added):
        """
        Add the specified amount to the current stock quantity.

        Args:
            amount_added (int): The number of units to add to inventory.
        """
        # Increase quantity by the amount specified
        self.quantity += amount_added
        print(f"Stock updated: {self.name} now has {self.quantity} units available.")

    def purchase_food(self, quantity):
        """
        Process a purchase of the specified quantity if stock is available.

        Decreases inventory on successful purchase; prints error if insufficient stock.

        Args:
            quantity (int): The number of units to purchase.
        """
        # Check if we have enough stock to fulfill the purchase
        if self.quantity >= quantity:
            print(
                f"Purchase successful! {quantity} units of {self.name} bought. We have {self.quantity - quantity} units left."
            )
            # Deduct the purchased quantity from inventory
            self.quantity -= quantity
        else:
            # Inform customer that insufficient stock is available
            print(
                f"Not enough stock! Only {self.quantity} units of {self.name} available."
            )


# ===== EXAMPLE USAGE =====
# Create two pet food instances
food1 = PetFood("Chicken Bites", "Purina", 10, 30)
food2 = PetFood("Carrot Mix", "Oxbow", 8, 15)

# Test purchase on food1: buy 5 units (should succeed)
food1.purchase_food(5)

# Add 10 units to food2's stock
food2.update_stock(10)

# Test purchase on food2: try to buy 20 units (should fail—only 25 available)
food2.purchase_food(20)
