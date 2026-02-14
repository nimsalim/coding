# Create a class named PetPost with the attributes name, species, age, adoption_fee, and description
class PetPost:
    name = ""
    species = ""
    age = 0
    adoption_fee = 0
    description = ""
    num_likes = 0


# Create first pet post
post1 = PetPost()
post1.name = "Max"
post1.species = "Dog"
post1.age = 3
post1.adoption_fee = 150
post1.description = (
    "Max is a friendly and energetic Golden Retriever looking for a loving home!"
)
post1.num_likes = 1000

# Create second pet post
post2 = PetPost()
post2.name = "Whiskers"
post2.species = "Cat"
post2.age = 2
post2.adoption_fee = 100
post2.description = "Whiskers is a playful Siamese cat who loves attention and cuddles."
post2.num_likes = 15

# Print details of the first pet post
print("Post 1:")
print(f"Name: {post1.name}")
print(f"Species: {post1.species}")
print(f"Age: {post1.age} years old")
print(f"Adoption Fee: ${post1.adoption_fee}")
print(f"Description: {post1.description}")
print()

# Print details of the second pet post
print("Post 2:")
print(f"Name: {post2.name}")
print(f"Species: {post2.species}")
print(f"Age: {post2.age} years old")
print(f"Adoption Fee: ${post2.adoption_fee}")
print(f"Description: {post2.description}")
