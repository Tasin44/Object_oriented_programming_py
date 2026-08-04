class Person:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def __add__(ref1,ref2):
        if isinstance(ref2,Person):
            tage=ref1.age+ref2.age
            tweight=ref1.weight+ref2.weight
            jointname=ref1.name+ref2.name
        else:
           raise TypeError("Unsupported operand type for +")
'''
If you use return instead of raise,
the code will still work fine, but it changes the behavior of the __add__ method slightly.
Both approaches are valid, but they convey different intentions:
(i)Using return indicates that the addition operation is performed and returns a result.
(ii)Using raise indicates that the addition operation cannot be performed due to incompatible types, 
and it raises an exception.
'''

# Define a class that is not an instance of Person
class Animal:
    def __init__(self,species) -> None:
        self.species=species

# Create instances of Person and Animal classes
person1=Person("Kamal",25,80)
animal1=Animal("Dog")

# Try to use the + operator with an instance of Animal
try:
    result=person1+animal1
    print("Final result: ",result)
except TypeError as e:
    print("Error:",e) 


# By raising a TypeError in this case, you're providing 
# clear feedback to the user that the operation they attempted is not 
# supported for the given operands. 



