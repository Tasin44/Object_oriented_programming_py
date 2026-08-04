
# in Python (and most object-oriented languages), "instance" and "object" mean the same thing in practical use. They are often used interchangeably.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Mustang", 2019)
'''
An instance is created from a class, which serves as a blueprint or template for the objects.

Here, car1 and car2 are instances(objects) of the Car class. 
Each instance has its own unique values for the make, model, and year attributes.

'''
