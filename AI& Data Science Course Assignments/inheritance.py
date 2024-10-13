# Inheritance is a feature of OOP that allows one class to inherit attributes and methods from another class.
# The class that inherits is called the "child" or "subclass," and the class being inherited from is the "parent" or "superclass."

# Example of Inheritance in Python:
class Animal:
    # Parent class (Animal)
    def __init__(self, name):
        self.name = name  # Attribute (name of the animal)

    def sound(self):
        print("Some generic animal sound.")

# Child class (Dog) inherits from Parent class (Animal)
class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks.")

# Creating an object of the Dog class (which inherits from Animal)
dog1 = Dog("Buddy")

# Accessing the method of the child class
dog1.sound()