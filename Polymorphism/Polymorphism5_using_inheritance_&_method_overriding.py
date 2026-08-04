'''
🧠 What Is Method Overriding?
-Method overriding means: This process of re-implementing a method in the child class is known as Method Overriding. 
-In method overriding: A child class redefines a method from its parent class with the same name and signature.


>Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass.
>This allows the subclass to customize or completely replace the behavior of the method inherited from the superclass.
'''

# Base class
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method")

'''
The Animal class defines a method "speak" that raises a NotImplementedError. 
This(NotImplementedError) serves as an abstract method, which means that it is intended to be overridden in subclasses.
By raising NotImplementedError, 
you enforce that any subclass of Animal must provide its own implementation of the speak method.
'''

# Subclass Dog overrides make_sound
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

# Subclass Cat overrides make_sound
class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")

class Bird(Animal):
    pass  # Inherits everything as-is
  

# Create a list of Animal objects
# Runtime polymorphism in action
animals = [Dog(), Cat(), Bird()]

# Call the speak method on each object
'''
A loop iterates through the list and calls the speak method on each object.
Due to polymorphism, the correct speak method for each object type (either Dog or Cat) is called.
'''
for animal in animals:# Which version gets called depends on the actual object type
    animal.make_sound()


'''
Output:
Woof! Woof!
Meow! Meow!

Traceback (most recent call last):
  File "/main.py", line 77, in <module>
    animal.make_sound()
  File "/main.py", line 44, in make_sound
    raise NotImplementedError("Subclass must implement this method")
'''










