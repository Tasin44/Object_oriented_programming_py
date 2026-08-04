
'''
It is a mechanism that allows you to create a hierarchy of classes 
that share a set of properties and methods by deriving a class from another class. 
Inheritance is the capability of one class to derive or inherit the properties from another class. 
'''

'''
Python Inheritance Syntax:
Class BaseClass:---------------------------> means parent class
   {body}
Class DerivedClass(BaseClass):-------------> means Child class
   {body}
'''

#Single inheritance example - 1

'''
Single inheritance: When a child class inherits from only one parent class, 
it is called single inheritance. We saw an example above.
'''

'''
Step:1
Creating a Parent Class
A parent class is a class whose properties are inherited by the child class.
'''

class Person():
    def __init__(self,nam,ID):
        self.name=nam
        self.id=ID
    def display(self):
        return f'The name is : {self.name} and id number is : {self.id}'

emp=Person("Tasin",62)
print(emp.display())

'''
Step:2
Creating a Child Class
A child class is a class that drives the properties from its parent class. 

A child class needs to identify which class is its parent class. 
This can be done by mentioning the parent class name in the definition of the child class. 
Example: class subclass_name (superclass_name)
'''

#After above code:
class Emp(Person):
    def output(self):
        print("child class(which named Emp) is called")
    
obj=Emp("Moon",20062)#if I make instance for Person class instead of Emp class,then if I try to call child class(Emp) method (output()),then error will be:
#'Person' object has no attribute 'output'
print(obj.display())
obj.output()

'''
output for child class:
The name is : Moon and id number is : 20062
child class(Emp) function is called
'''

#Another Example:

class Animal:
    def __init__(self, name, age, sound):
        self.identity = name
        self.age = age
        self.speak = sound

    def create_sound(self):
        return f'Animal name: {self.identity}, age : {self.age}, and speaking sound: {self.speak}'

    def get_class_name(self):
        return self.__class__.__name__

class Cat(Animal):
    pass

class Cow(Animal):
    pass

wild = Cat("Ptcat", 2, "meow")
print(f'Class name: {wild.get_class_name()}')
print(wild.create_sound())

wild= Cow("Bramah", 4, "moo")
print(f'Class name: {wild.get_class_name()}')
print(wild.create_sound())


