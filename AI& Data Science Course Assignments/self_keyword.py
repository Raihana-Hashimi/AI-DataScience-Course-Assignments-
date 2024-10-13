# The 'self' keyword is used to refer to the instance of the class.
# It allows access to the attributes and methods of the class within its methods.

# Example of the 'self' keyword in Python:
class Person:
    def __init__(self, name, age):
        # 'self' refers to the object being created
        self.name = name  # Attribute (name)
        self.age = age  # Attribute (age)

    # Method using 'self' to refer to object attributes
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating an object of the Person class
person1 = Person("Alice", 25)

# Accessing the method of the object
person1.introduce()