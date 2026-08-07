'''
The __add__method can add only two object
What if we try to do:
'''
#    def __add__(self, other,third):
#            total_age = self.age + other.age+third.age
#            total_weight = self.weight + other.weight+third.weight
#            joint_name=self.name+other.name+third.name
#            return total_age, total_weight ,joint_name

obj1 = Person("Alim", 25, 90)
obj2 = Person("karim", 30, 60)
obj3 = Person("Zamal", 20, 50)

print(obj1 + obj2 + obj3) 
'''
❌ What's wrong:

Your current __add__ method takes three parameters:

    def __add__(self, other, third):  # ❌ Not allowed

But Python only supports binary addition (a + b), so __add__ must take exactly two arguments: self and other.

When you write:

    obj1 + obj2 + obj3

Python processes it as:

    (obj1 + obj2) + obj3

So it calls:

    obj1.__add__(obj2) → returns a result
    Then tries: result.__add__(obj3) → fails, because result is not a Person object

'''
#=====================================================================================================

'''
Correct approach
#if we want to add more than two objects:
'''

class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Person):
            tot_age = self.age + other.age
            tot_weight = self.weight + other.weight
            joint_name = self.name + other.name
            return Person(joint_name, tot_age, tot_weight)
        return NotImplemented

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}"

# Creating Person objects
obj1 = Person("Tasin", 29, 20)
obj2 = Person("Kamal", 25, 40)
obj3 = Person("Rahim", 30, 80)
obj4 = Person("Jamil", 55, 20)

result = obj1 + obj2 + obj3 + obj4
print(result)

'''
🔹 What happens when you return Person(...) inside __add__?

When you write:

        return Person(joint_name, total_age, total_weight)

You're telling Python to:

    Create a new Person object using the combined data.

    This calls the __init__ method again to initialize this new object.

    The new object is returned as the result of obj1 + obj2.

🔁 Why do this?

By returning a new Person, you allow expressions like:

        result = obj1 + obj2 + obj3

to work correctly. Here's how it executes internally:
Step-by-step:

    obj1 + obj2 → obj1.__add__(obj2) → returns a new Person with combined data.

    result + obj3 → now becomes Person.__add__(obj3) → again returns a new Person.

So this works recursively by always returning a new object of the same type (Person) — allowing further chaining.


🔁 Explanation of this line" This calls the __init__ method again to initialize this new object."
Is __init__ called again and again?

✅ Yes — but only for the new object being created, not for obj2 or obj3.
🔍 What exactly happens?

Let’s say you write:

result = obj1 + obj2 + obj3

This is evaluated in steps:
Step 1:

temp = obj1 + obj2
# Calls: obj1.__add__(obj2)
# Inside __add__:
#   total_age = 25 + 30
#   total_weight = 90 + 60
#   joint_name = "Alimkarim"
# Returns: Person("Alimkarim", 55, 150) ➜ __init__ is called **once**

Step 2:

result = temp + obj3
# Calls: temp.__add__(obj3)
# Inside __add__:
#   total_age = 55 + 20
#   total_weight = 150 + 50
#   joint_name = "AlimkarimZamal"
# Returns: Person("AlimkarimZamal", 75, 200) ➜ __init__ is called **again**

🧠 Important Note:

    obj1, obj2, obj3 — already created, __init__ is not called again for them.

    Only for the new result objects being created inside __add__, __init__ is called again to initialize those new objects.


'''
#===============================================================================================================

'''
# Chaining additions
#If we try to do like:
'''
#       result = obj1 + obj2 + obj3 + obj4 + 7  # This will raise a TypeError

# Printing the result
#       print(result)
'''
If you try to add a Person object to an integer like 7 
(i.e., result = obj1 + obj2 + obj3 + obj4 + 7), 
the absence of the "if isinstance(other, Person)" check 
and the "return NotImplemented" statement in the __add__ method 
will cause a runtime error because the __add__ method's addition operation 
expects another Person object(like obj5).

Here’s what will happen step by step:

Adding obj1 and obj2:
intermediate1 = obj1 + obj2  # This creates a new Person object

Adding intermediate1 and obj3:
intermediate2 = intermediate1 + obj3  # This creates another new Person object

Adding intermediate2 and obj4:

intermediate3 = intermediate2 + obj4  # This creates yet another new Person object

Attempting to Add intermediate3 and 7:

result = intermediate3 + 7  # This will cause an error

Here's what the error might look like:
AttributeError: 'int' object has no attribute 'age'

but if we use return NotImplemented,then will occur type error
TypeError: unsupported operand type(s) for +: 'Person' and 'int'

'''

