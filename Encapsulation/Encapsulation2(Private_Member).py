'''
Private Members
Private members are those that should not be accessed directly outside the class. 
In Python, private members are defined by prefixing the member name with two underscores (__).
In Python, there is no existence of Private instance 
variables that cannot be accessed except inside a class.
'''
class MyClass:
    def __init__(self):
        self.__private_attribute = 42  # Private attribute
        self.public_attribute = "Hello"  # Public attribute

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("This is a public method.")
        self.__private_method()  # Accessing private method within the class

obj = MyClass()
print(obj.public_attribute)  # This will work
# print(obj.__private_attribute)  # This will raise an AttributeError

obj.public_method()  # This will work
# obj.__private_method()  # This will raise an AttributeError

# Name mangling,it allows access, but it's not recommended because it breaks encapsulation.
print(obj._MyClass__private_attribute)
obj._MyClass__private_method()
'''
_classname__, where classname is the current class name with a leading underscore
'''
