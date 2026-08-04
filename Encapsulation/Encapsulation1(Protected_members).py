'''
🔐 Main Concept of Encapsulation :

    Bundles data (attributes) and methods (functions) into a single unit (class).
    Restricts direct access to some components, hiding internal implementation details.
This protects the internal state of an object by:

    Hiding internal details from the outside world.

    Allowing controlled access through methods.

    Preventing accidental modification of important data.

In Python, this is done using access modifiers:

    Public: accessible everywhere.

    Protected (_): should be accessed only within the class or subclass.

    Private (__): hidden from outside access.
    

Protected Members:
Protected members are those that are intended to be accessed only within the class 
and its subclasses.
In Python, protected members are defined by prefixing the member 
name with a single underscore (_).

'''
"""
*************************
If you want to access private attributes or private methods outside of their defining class (even in a child class), 
you must use the name-mangled format, which is _ParentClassName__attribute or _ParentClassName__method().

This is because Python uses name mangling to make private members "inaccessible" outside the defining class. 
***********************
"""
#In Python,encapsulation is achieved using private and protected members.

'''
Examples of Protected and private attribute in Encapsulation :
'''

#EXAMPLE-1(Protected Attribute )
class Protected:
    def __init__(self):
        self._age = 30  # Protected attribute, it's accessible in it's own class

class Subclass(Protected):
    def display_age(self):
        self._age+=3 # Protected attribute is also Accessible in subclass
        print(self._age)
        
obj = Subclass()#must be call the subclass always 
obj.display_age() # This method within the subclass accesses the protected attribute and prints its value. 

'''
Why not I create _init_ on the subclass?
Subclass doesn't define its own __init__, so it automatically uses the __init__ from the parent class (Protected).
That means _age is still initialized properly.
✅ You can access _age in the subclass because it's inherited.
'''
========================================================================================================================================================================


#EXAMPLE-2(Protected Attribute access with the classname )
class Base(object):
    def __init__(self):
        self._a=2
class derived(Base):
    def __init__(self):
       Base.__init__(self)#name mangling
       print("Calling protected member of base class: ",self._a)
       self._a+=3
       print("Calling protected member of child class: ",self._a)

obj1=derived()
'''
------------------Example 1

Subclass does not define its own __init__.

So Python automatically uses the parent class (Protected) __init__.

_age is initialized from the parent, then modified inside display_age().

----------------Example 2

-Subclass defines its own __init__.

-When a child class has its own constructor, parent __init__ is NOT called automatically.

-So we manually call it.
    
Why use __init__ in code 2?

-You use it when the child class needs its own initialization logic.

------------Example future advantages:

-Add new attributes in subclass

-Modify parent values during creation

-Run extra setup when object is created

like in example 2 future work:
'''
class Subclass(Protected):
    def __init__(self):
        super().__init__()
        self.name = "Tasin"


========================================================================================================================================================================

# Example -3 (Private Attribute) 

class Base:
    def __init__(self):
        self.__privateattribute=5

class derived(Base):

    def __init__(self):
        Base.__init__(self)
        print("Calling private attribute of Base Class: ",self._Base__privateattribute)
        self._Base__privateattribute+=7
        print("Calling private attribute of Child class: ",self._Base__privateattribute)
    
obj=derived()

# output:
# Calling private attribute of Base Class:  5
# Calling private attribute of Child class:  12



# ===========================================================================================================================================================================
# ===========================================================================================================================================================================

'''
#                                                                     super method:

✅Main Use Case: super() lets you call a parent class’s methods or constructor (__init__) in child class without explicitly naming the parent class.

✅Private Members Limitation: It cannot directly access private attributes/methods(starting with double __) due to Python’s name-mangling. 
✅Protected Attributes Limitation:super() is not used to directly access protected attributes like self._b.
You access those via methods (e.g., getter functions) if needed.

Key Takeaways:
    ✅Used for inheritance (calling parent class methods).
    ✅Avoids hardcoding the parent class name.
    ✅✅✅Works with protected/public methods, not works for private method or private/protected attributes.
'''

'''
Connection Between Encapsulation & super()

    Encapsulation protects data inside a class.
    super() accesses inherited methods while respecting encapsulation (cannot bypass private members).
'''

class BaseClass:
    def __init__(self):
        self._protected_attribute = 42  # Protected attribute

    def _protected_method(self):
        print("This is a protected method.")

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        print(self._protected_attribute)  # Accessing protected attribute
        self._protected_method()  # Accessing protected method

obj = DerivedClass()
print(obj._protected_attribute)  # This will work, but it's not recommended
obj._protected_method()  # This will work, but it's not recommended

'''
In the above example:
# _protected_attribute and _protected_method are protected members.
# Protected members can be accessed within the class and its subclasses.
# Accessing protected members outside the class or its subclasses is technically allowed but is discouraged.
'''



========================================================================================================================================================================


# Example 2 : Super()
class Parent:
    def __init__(self):
        self.__private = "Private Attribute"
        self._protected = "Protected Attribute"
    
    def __private_method(self):
        print("Parent's Private Method")
    
    def _protected_method(self):
        print("Parent's Protected Method")

    def public_method(self):
        print("Parent's Public Method")

class Child(Parent):
    def show(self):
        # Call protected method
        super()._protected_method()

        # Call public method
        super().public_method()

        # The following will cause an error:
        
        # print("Protected Attribute:", super()._protected)
        # super().__private  # ❌ AttributeError
        # super().__private_method()  # ❌ AttributeError

        # To access private members, we should use name mangling,but it's not recommended because it breaks encapsulation:
        print("Private Attribute (via name mangling):", self._Parent__private)#Accessing private attribute outside of the class
        self._Parent__private_method()#Accessing private method outside of the class

obj = Child()
obj.show()



