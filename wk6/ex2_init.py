class PetPost:
    def __init__(
        self, pet_name, pet_type, pet_age, adoption_fee, description, num_likes
    ):
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.pet_age = pet_age
        self.adoption_fee = adoption_fee
        self.description = description
        self.num_likes = num_likes

    def display_info(self):
        print(f"Pet Name: {self.pet_name}")
        print(f"Pet Type: {self.pet_type}")
        print(f"Pet Age: {self.pet_age} years")
        print(f"Adoption Fee: ${self.adoption_fee}")
        print(f"Number of Likes: {self.num_likes}")
        print(f"Description: {self.description}")


post1 = PetPost(
    input("Enter pet name: "),
    input("Enter pet type: "),
    int(input("Enter pet age: ")),
    int(input("Enter adoption fee: ")),
    input("Enter description: "),
    int(input("Enter number of likes: ")),
)
print("Pet Post 1:")
post1.display_info()
