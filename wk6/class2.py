class Bike:
    wheels = 2

    def __init__(self, frame_size, color):
        self.frame_size = frame_size
        self.color = color

    def ring_bell(self):
        print("Ring ring!")


my_bike = Bike(42, "red")
your_bike = Bike(48, "blue")
their_bike = Bike(50, "green")
print(my_bike.wheels)
print(my_bike.frame_size)
print(my_bike.color)
my_bike.ring_bell()
