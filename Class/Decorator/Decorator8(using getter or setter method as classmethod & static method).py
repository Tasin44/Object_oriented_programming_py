# 1. Using @classmethod for Getters/Setters
'''A @classmethod can access and modify class-level attributes (shared across all instances).'''
class Employee:
  __default_role="Admin"# Class-level attribute
  
  def __init__(self,role=None):
    self.role=role if role else Employee.__default_role
  
  @classmethod
  def get_role(cls):# Getter for class attribute
    return cls.__default_role
    
  @classmethod
  def set_role(cls,new_role):# Setter for class attribute
    cls.__default_role=new_role

print(Employee.get_role())
Employee.set_role("Doctor")# Changes class-level default
obj=Employee()
print(obj.role)
  
# output:

# Admin
# Doctor


====================================================================================================================================================================================================================================

# 2. Using @staticmethod for Getters/Setters
'''A @staticmethod doesn’t access self or cls and is used for logic that doesn’t depend on class/instance state.'''

'''
While @staticmethod isn’t typically used for standard Python getters and setters (like with @property), you can create manual-style getter and setter methods using @staticmethod — 
especially for utility-like or external variable management (e.g., shared configuration, validation, caching logic, etc.).
'''

class Bank:
  __rate={}#prive class level dict
  
  @staticmethod
  def set_rate(key,value):
    Bank.__rate[key]=value
  
  @staticmethod
  def get_rate(key):
    return Bank.__rate.get(key,f"Not Found The key {key}")

Bank.set_rate("interest_rate",2.50)
Bank.set_rate("Deposit_rate",3.00)

print(Bank.get_rate("interest_rate"))
print(Bank.get_rate("Deposit_rate"))
print(Bank.get_rate("loan"))

# Output:
# 2.5
# 3.0
# Not Found The key loan

====================================================================================================================================================================================================================================

#without staticmethod
class Employee:
    __name_dict = {}

    def set_name(self, key, name):
        Employee.__name_dict[key] = name

    def get_name(self, key):
        return Employee.__name_dict.get(key, f"Not found {key}")

# Create an object
emp = Employee()
emp.set_name("Name", "Tasin")
print(emp.get_name("Name"))  # ✅ Output: Tasin

'''
But if we do like:

Employee.set_name("Name", "Tasin")    # ❌
print(Employee.get_name("Name"))      # ❌

But set_name and get_name are defined to use self, which means they are instance methods, and must be called on an object, not directly on the class.

'''

#with staticmethod
#Or if we really want to call them using classname
#Make methods @staticmethod so they can be called using the class
class Employee:
    __name_dict = {}

    @staticmethod
    def set_name(key, name):
        Employee.__name_dict[key] = name

    @staticmethod
    def get_name(key):
        return Employee.__name_dict.get(key, f"Not found {key}")

# Call using the class
Employee.set_name("Name", "Tasin")
print(Employee.get_name("Name"))  # ✅ Output: Tasin




====================================================================================================================================================================================================================================
