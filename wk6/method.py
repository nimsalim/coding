class Pet:
    def __init__(self, name, species, age, adoption_fee):
        self.name = name
        self.species = species
        self.age = age
        self.adoption_fee = adoption_fee

    def show_details(self):
        print(
            f"{self.name} is a {self.species}, {self.age} years old, and costs ${self.adoption_fee} for adoption."
        )


pet1 = Pet("Buddy", "Dog", 3, 150)
pet2 = Pet("Whiskers", "Cat", 2, 100)
pet1.show_details()
pet2.show_details()
