# An object is an instance of a class.
# It is a specific "thing" created from the blueprint of a class.

# Example of an object in Python:
class Car:
    # Constructor to initialize car attributes
    def __init__(self, brand, color):
        self.brand = brand  # Attribute (brand of the car)
        self.color = color  # Attribute (color of the car)

    # Method to drive the car
    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")

# Creating an object (instance) of the Car class
car1 = Car("Toyota", "red")

# Accessing the method of the object
car1.drive()