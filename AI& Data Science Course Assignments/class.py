# A class is a blueprint or template for creating objects.
# It defines attributes (properties) and methods (actions) for those objects.

# Example of a class in Python:
class Dog:
    # Constructor method to initialize the attributes
    def __init__(self, name, breed):
        self.name = name  # Attribute (name of the dog)
        self.breed = breed  # Attribute (breed of the dog)

    # Method to make the dog bark
    def bark(self):
        print(f"{self.name} is barking!")

# Creating an object (instance) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")

# Accessing the method of the object
dog1.bark()