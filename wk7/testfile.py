# print hello world
print("HW")


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print("The average is: " + str(result))
