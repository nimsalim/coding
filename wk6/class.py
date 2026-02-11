class Bike:
    wheels = 2
    frame_size = 42
    color = "red"


new_bike = Bike()

print(new_bike.wheels)
print(new_bike.frame_size)
print(new_bike.color)

your_bike = Bike()
their_bike = Bike()
print(your_bike.wheels)

your_bike.color = "blue"
print(your_bike.color)
your_bike.frame_size = 48
print(your_bike.frame_size)
print(new_bike.frame_size)
