pet_names = ["Buddy", "Mittens", "Rex", "Whiskers"]


def pet_says(name, sound):
    print(f"{name} says {sound}!")


pet_says("Buddy", "woof")

pet_says(sound="Woof", name="Buddy")


# Processing Daisy's litter
daisy_weights = [1.00, 1.14, 1.06, 1.1, 1.03, 1.17]
daisy_sum = 0
for weight in daisy_weights:
    daisy_sum += weight
daisy_average = daisy_sum / len(daisy_weights)
print(f"Daisy's litter average weight: {daisy_average:.2f} lbs")
if daisy_average >= 1.0:
    print("Daisy's litter is healthy")
else:
    print("Daisy's litter needs attention")

# Processing Luna's litter
luna_weights = [0.92, 0.97, 0.86, 0.90, 0.95]
luna_sum = 0
for weight in luna_weights:
    luna_sum += weight
luna_average = luna_sum / len(luna_weights)
print(f"Luna's litter average weight: {luna_average:.2f} lbs")
if luna_average >= 1.0:
    print("Luna's litter is healthy")
else:
    print("Luna's litter needs attention")


def calculate_average_weight(weights):
    """Accepts a list of weights and returns the average weight"""
    return sum(weights) / len(weights)


def assess_litter_health(average_weight):
    """Accepts an average weight of a litter in lbs and reviews whether the litter is healthy"""
    if average_weight >= 1.0:
        return "is healthy"
    else:
        return "needs attention"


def process_litter(litter_name, weights):
    """Assesses the litter's health and prints the results"""
    average_weight = calculate_average_weight(weights)
    health_status = assess_litter_health(average_weight)
    print(f"{litter_name}'s litter average weight: {average_weight:.2f} lbs")
    print(f"{litter_name}'s litter {health_status}")


# Processing litters is now much cleaner
process_litter("Daisy", [1.00, 1.14, 1.06, 1.1, 1.03, 1.17])
process_litter("Luna", [0.92, 0.97, 0.86, 0.90, 0.95])
