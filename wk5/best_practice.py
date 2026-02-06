with open("../data/pet_store_inventory.txt", "r") as file:
    # Read the entire content of the file
    content = file.read()
    # Print the content
    print("file content:\n")
    print(content)


with open("pet_store_inventory.txt", "r") as inventory:
    content = inventory.read()
    print(content)


with open("daily_inventory.txt", "w") as file:
    file.write("Dog Food - 50 bags\n")
    file.write("Cat litter - 10 boxes\n")
    file.write("Bird Seed - 25 packs\n")
print("Inventory file has been created.")

with open("../data/daily_inventory.txt", "a") as file:
    file.write("Fish Food - 15 bags\n")
    print("Fish Food added to inventory file.")


with open("sales_log.txt", "a") as file:
    file.write("Sold 5 bags of Dog Food\n")
    file.write("Sold 2 boxes of Cat Litter\n")

print("Sales data has been recorded.")
