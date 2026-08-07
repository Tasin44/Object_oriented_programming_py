'''
Definition:
Abstraction is the concept of hiding the complex implementation details of a system and 
exposing only the necessary parts to the user. It helps in reducing complexity and 
allows the programmer to focus on interactions at a high level.
'''
# It means hiding complex things behind a procedure so that things look simiple 

'''
❓Does method overriding and abstract method means same?

Method overriding: A child class provides its own implementation of a method that already exists in the parent class.
@abstractmethod: It is not method overriding. It is a declaration that says, "Every concrete child class must implement this method.
'''


from abc import ABC, abstractmethod

# Define an abstract base class
class Animal(ABC):
    
    @abstractmethod
    def speak(self):
        """This Abstract method that must be implemented by subclasses."""
        pass

    @abstractmethod
    def move(self):
        """This Another abstract method that must be implemented by subclasses."""
        pass

# Subclass that inherits from the abstract base class
class Dog(Animal):
    
    def speak(self):
        return "Woof!"

    def move(self):
        return "Runs on four legs"

# Another subclass
class Bird(Animal):
    
    def speak(self):
        return "Chirp!"

    def move(self):
        return "Flies in the sky"

# Instantiating subclasses and using them
dog = Dog()
print(dog.speak())  # Output: Woof!
print(dog.move())   # Output: Runs on four legs

bird = Bird()
print(bird.speak())  # Output: Chirp!
print(bird.move())   # Output: Flies in the sky

'''
Explanation
Key Points

(i) Abstract Class: A class that contains one or more abstract methods and cannot be instantiated.

(ii) Abstract Method: An abstract method is the one which cannot be called but can be overridden. 
You need to decorate it with @abstractmethod decorator.
Subclasses must override and implement these methods.

(iii) The abc Module: Provides tools to define abstract base classes in Python.

ABC is the base class for defining abstract base classes, and abstractmethod is the decorator for marking methods as abstract.

1.Importing ABC and abstractmethod:
"from abc import ABC, abstractmethod" 
imports the necessary components to define abstract base classes and abstract methods.

2.The statement from abc import ABC, abstractmethod is used to 
import the ABC class and the abstractmethod decorator from the abc module in Python. 

(i) abc module:
#  The abc module in Python stands for "Abstract Base Classes."
#  It provides the infrastructure for defining abstract base classes, 
   which are classes that cannot be instantiated and are meant to be subclassed by other classes.
#  The abc module is part of Python's standard library, so you don't need to install 
   any additional packages to use it.

(ii) ABC class:
#  The ABC class is a helper class provided by the abc module.
#  When you create a class that inherits from ABC, you are defining an abstract base class.
#  Abstract base classes are used to define a common interface for a group of related classes,
   but cannot be instantiated themselves.

(iii) abstractmethod decorator:
#  The abstractmethod decorator is used to declare abstract methods within an abstract base class.
#  An abstract method is a method that is declared in the abstract base class, but does not have an 
   implementation.
#  Subclasses of the abstract base class are required to provide implementations 
   for all abstract methods.

'''
