# 1. Method Overriding (Supported in Python) ✅

# Definition:
# When a child class writes its own version of a method that already exists in the parent class.

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):      # Overrides parent's sound()
        print("Bark")

d = Dog()
d.sound()

# Output:

# Bark

# Easy way to remember:

# Parent says one thing, child replaces it with its own version.