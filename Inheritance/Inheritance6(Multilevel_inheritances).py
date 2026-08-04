
'''
Multilevel inheritance: When we have a child and grandchild relationship. 
This means that a child class will inherit from its parent class, 
which in turn is inheriting from its parent class.
'''

'''
Base or Super class. Note object in bracket.
(Generally, object is made ancestor of all classes)
In Python 3.x "class Person" is equivalent to "class Person(object)"
'''
# Base → Child → GrandChild

class Base(object):
	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name


# Inherited or Sub class (It's parent class name in bracket)
class Child(Base):
	# Constructor
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	# To get age
	def getAge(self):
		return self.age


# Inherited or Sub class (It's parent class name in bracket)
class GrandChild(Child):
	# Constructor
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	# To get address
	def getAddress(self):
		return self.address


g = GrandChild("Abdur Rahman", 55 , "Noida")
print(g.getName(), g.getAge(), g.getAddress())

# output:
# Abdur Rahman 55 Noida

==============================================================================================================================================================
'''
using super() method 

❌ This line is incorrect:
	super().__init__(self, name)
Why it's wrong: super().__init__() automatically passes self — you do not need to (and should not) pass it explicitly.

Correct usage: Just use super().__init__(name)
'''

class Base(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Child(Base):
    def __init__(self, name, age):
        super().__init__(name)  # ✅ No need to pass `self`
        self.age = age

    def getAge(self):
        return self.age


class GrandChild(Child):
    def __init__(self, name, age, address):
        super().__init__(name, age)  # ✅ No need to pass `self`
        self.address = address

    def getAddress(self):
        return self.address


# Test
g = GrandChild("Abdur Rahman", 55, "Noida")
print(g.getName(), g.getAge(), g.getAddress())



====================================================================================================================================================================


# Another example of Multilevel Inheritance

Person → Employee → Manager
# Base class
class Person:
    def __init__(self, name):
        self.name = name
        print("Person initialized")

    def get_name(self):
        return self.name

# Intermediate class
class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)  # Calls Person's constructor
        self.employee_id = employee_id
        print("Employee initialized")

    def get_employee_id(self):
        return self.employee_id

# Derived class
class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)  # Calls Employee's constructor
        self.department = department
        print("Manager initialized")

    def get_department(self):
        return self.department

# Creating an object of the most derived class
m = Manager("Sarah", "EMP123", "HR")

# Accessing methods from all levels
print("\n--- Accessing inherited data ---")
print("Name:", m.get_name())            # from Person
print("Employee ID:", m.get_employee_id())  # from Employee
print("Department:", m.get_department())    # from Manager


# Output:
# Person initialized
# Employee initialized
# Manager initialized

# --- Accessing inherited data ---
# Name: Sarah
# Employee ID: EMP123
# Department: HR







