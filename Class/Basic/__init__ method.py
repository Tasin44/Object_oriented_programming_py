##See details in docs
#to know more: https://www.geeksforgeeks.org/constructors-in-python/
# in Python (and most object-oriented languages), "instance" and "object" mean the same thing in practical use. They are often used interchangeably.

class Person: 
    def __init__(self,name,age,company):
        self.name=name
        self.age=age
        self.company=company
    
p1=Person("Tasin",25,"Enosis")#Person is the class,p1 is an object (an instance of the Person class)
print(p1.age)
print(p1.name)

# In Python, the __init__ method is similar to a constructor in C++. 
# The __init__ method is a special method that is automatically called ,
# when an instance of the class is created. It allows you to initialize the attributes of the class.
# You can define it to perform any initialization actions required for the object.

'''
we cannot have two __init__ methods with the same name in a single class in Python. 
Python does not support method overloading based on the number or types of arguments, 
unlike some other programming languages.
'''

'''
An "empty class" in the context means a class that is defined 
without any methods, including __init__. 
However, it is entirely possible to define any class without an __init__ method, 
not just empty ones. The presence or absence of the __init__ method 
does not depend on whether the class is empty or not.
'''

#Example of an Empty Class Without __init__
# Use the pass keyword when you do not want to add any other properties or methods to the class.
class EmptyClass:
    pass

instance = EmptyClass()
print(instance)  # Outputs: <__main__.EmptyClass object at 0x...>


#Example of a Class With Other Methods But Without __init__

class MyClass:
    def some_method(self):
        print("This is a method in MyClass")

instance = MyClass()
instance.some_method()  # Outputs: This is a method in MyClass

'''
We can define class in the below ways:

1.class Person:       # ✅ Recommended
    pass

2.class Person():     # ✅ Also valid
    pass

3.class Person(object):  # ✅ Explicit inheritance from object (good in Python 2, optional in Python 3)
    pass

In Python 3.x "class Person" is equivalent to "class Person(object)"
'''

