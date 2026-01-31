Best practices for writing functions

When developing Python functions, it's crucial to follow best practices to make sure your code is clean, efficient, and maintainable. In this lesson, you will understand how functions can be used to make your code logical and maintainable.

The following example demonstrates the benefits of using functions. Two dogs in a pet shelter, Daisy and Luna, recently gave birth. You create a program that checks the health of a litter of puppies by calculating their average weights and determining if they are above or below average.



CONTINUE
# Processing Daisy's litter
daisy_weights = [1.00, 1.14, 1.06, 1.1, 1.03, 1.17]
daisy_sum = 0
for weight in daisy_weights:
   daisy_sum += weight
daisy_average = daisy_sum  / len(daisy_weights)
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
