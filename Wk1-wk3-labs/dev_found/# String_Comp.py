# String_Comp
print("Apple" < "Banana")  # True - Apple comes before Banana alphabetically
print("Grape" > "Cherry")  # True - Grape comes after Cherry alphabetically
print("Mango" == "Mango")  # True - Both strings are identical
print(
    "Orange" != "orange"
)  # True - Orange and orange are different strings due to case sensitivity
# Comparing numbers
hamster_age = 2
print(hamster_age >= 1)  # True
print(hamster_age >= 3)  # False

# Comparing strings (based on alphabetical order)
dog_name = "Luna"
print(dog_name > "Bella")  # True - Luna comes after Bella alphabetically
print(dog_name == "Luna")  # True - Names match exactly

# Comparing with variables
cat_price = 30
fish_price = 25
print(cat_price > fish_price)  # True - Cats cost more than fish
print(cat_price == fish_price)  # False - Prices are different


# logical operators
x = 5
y = 10
print(x < 10 and y > 5)  # True - both conditions are true
print(x < 10 or y < 5)  # True - at least one condition is true
