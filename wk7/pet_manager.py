def add_pet(self, name, species, age, color):  # Modified
    pet_id = str(self.next_id)
    self.pets[pet_id] = {
        "name": name,
        "species": species,
        "age": age,
        "color": color,  # New field
        "adopted": False,
        "date_added": datetime.now().strftime("%Y-%m-%d"),
    }
    self.next_id += 1
    print(f"Pet added successfully with ID: {pet_id}")
