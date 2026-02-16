def display_pets(pets):
    if not pets:
        print("No pets in the system.")
        return

    print("\nCurrent Pets:")
    print(
        "ID | Name | Species | Age | Color | Status | Added Date"
    )  # Added color header
    print("-" * 85)

    for pet_id, pet in pets.items():
        status = "Adopted" if pet["adopted"] else "Available"
        print(
            f"{pet_id:<4}| {pet['name']:<10}| {pet['species']:<10}| {pet['age']:<4}| \
              {pet['color']:<10}| {status:<10}| {pet['date_added']}"
        )  # Add color header
