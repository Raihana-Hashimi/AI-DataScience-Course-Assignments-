# A constructor is a special method that is automatically called when an object is created.
# It is used to initialize the attributes of the object.

# Example of a constructor in Python:
class Student:
    # Constructor to initialize student attributes
    def __init__(self, name, age):
        self.name = name  # Attribute (name of the student)
        self.age = age  # Attribute (age of the student)

    # Method to display student information
    def show_info(self):
        print(f"Student: {self.name}, Age: {self.age}")

# Creating an object (instance) of the Student class
student1 = Student("Alice", 20)

# Accessing the method of the object
student1.show_info()