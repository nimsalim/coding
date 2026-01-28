# Pet inventory

pet_inventory = {"dog_food": 10, "cat_food": 8, "fish_tanks": 3, "bird_cages": 5}

print(pet_inventory["dog_food"])
print(pet_inventory["bird_cages"])

pet_inventory = {"dog_food": 10, "cat_food": 8, "fish_tanks": 3, "bird_cages": 5}
if "hamster_wheels" in pet_inventory:
    print(pet_inventory["hamster_wheels"])
else:
    print("Sorry, we dont carry that item.")


inventory = {"apples": 5, "bananas": 4, "coconuts": 2, "dates": 10}

if "bananas" in inventory:
    num_bananas = inventory["bananas"]
    print(f"There are {num_bananas} bananas available!")

inventory = {"apples": 5, "bananas": 4, "coconuts": 2, "dates": 10}

print(inventory.get("apples"))
print(inventory.get("Apples"))


inventory = {"apples": 5, "bananas": 4, "coconuts": 2, "dates": 10}

print(inventory.get("elderberries", 0))
print(inventory.get("coconuts", 0))
