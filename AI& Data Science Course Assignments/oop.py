# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes.
# It allows us to model real-world things using attributes (data) and methods (functions).

# Example of OOP in Python:
class Person:
    # Constructor to initialize person attributes
    def __init__(self, name, age):
        self.name = name  # Attribute (name of the person)
        self.age = age  # Attribute (age of the person)

    # Method for greeting
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object (instance) of the Person class
person1 = Person("John", 30)

# Accessing the method of the object
person1.greet()