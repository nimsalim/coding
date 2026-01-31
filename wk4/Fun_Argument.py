def my_function(food="Spagetti"):
    print("My favorite food is " + food)


"""
Print a message about the programmer's favorite food.
"""

# call function with 'pizza' as an argument.
my_function("pizza")

# call function with 'tacos' as an argument.
my_function("tacos")

# call function with no argument.
my_function()


def my_friend(friend_name, friend_city, friend_age=25):  # type: ignore
    """
    Takes in two parameters, `friend_name` and `friend_city`,
    and print a message stating your friend with name `friend_name`
    lives in `friend_city`.
    """

    print(
        f"My friend {friend_name} lives in {friend_city} and is {friend_age} years old."
    )


# You can get unexpected results if you change the order of the arguments when calling your function. For example, go back to your code and adjust the last line so that Python calls the city of residence first and the name second. Then, re-run your script.

my_friend("Souleymane", "New York")


def my_friend(friend_name, friend_city, friend_age=25):
    """
    Takes in two parameters, `friend_name` and `friend_city`,
    and print a message stating your friend with name `friend_name`
    lives in `friend_city`.
    """

    print(
        f"My friend {friend_name} lives in {friend_city} and is {friend_age} years old."
    )


# Get input from user
name = input("Enter friend's name: ")
city = input("Enter friend's city: ")
age = input("Enter friend's age: ")

my_friend(name, city, int(age))
