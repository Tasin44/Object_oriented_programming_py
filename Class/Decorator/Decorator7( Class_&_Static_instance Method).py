#If data belongs to an object → NOT static
#If data belongs to the class as a whole → static

#static data holo cls level data, object level data na means kono specific object er data na
#=================================================================================================================================================================================
# Static variable and static method:
#                                                                                  Static Variable (Class Variable)

# A variable that is shared by all objects of the class. It belongs to the class, not to individual objects.

class Hospital:
    hospital_name = "Dhaka MC"   # Static/Class variable

h1 = Hospital()
h2 = Hospital()

print(h1.hospital_name)  # Dhaka MC
print(h2.hospital_name)  # Dhaka MC

# If you change it through the class:

Hospital.hospital_name = "City Hospital"

print(h1.hospital_name)  # City Hospital
print(h2.hospital_name)  # City Hospital

#                                                                                    Static Method

# A method that doesn't need self or cls. It's used for utility/helper functions related to the class.

class Hospital:

    @staticmethod
    def is_valid_id(pt_id):
        return pt_id > 0

print(Hospital.is_valid_id(10))   # True
print(Hospital.is_valid_id(-5))   # False

# Easy way to remember
# Static/Class Variable → Shared data for all objects.
# Static Method → Shared helper function that doesn't access object (self) or class (cls) data.


#==================================================================================================================================================================================
#                                                                                                            '''
#                                                                                        Final Exmaple of class,instance and static method 
#                                                                                                            '''
# Here’s a very simple, real-life example using a BankAccount class so you clearly understand:
# ✅ Instance Method
# ✅ Class Method
# ✅ Static Method

#🎯 Easy Way to Remember
#-If it needs object data → Instance method
#-If it needs class-level data → Class method
#-If it needs no class or object data → Static method

#code : 

class BankAccount:
    # 👉 Class variable (shared by all accounts)
    bank_name = "ABC Bank"
    total_accounts = 0

    # 👉 Constructor (runs when object is created)
    def __init__(self, owner, balance):
        self.owner = owner          # Instance variable (belongs to object)
        self.balance = balance      # Instance variable
        BankAccount.total_accounts += 1  # Increase total accounts

    # ===============================
    # 1️⃣ Instance Method
    # ===============================
    def deposit(self, amount):
        """
        Instance method:
        - Works with object data (self)
        - Can access instance variables
        """
        self.balance += amount
        return f"{self.owner} new balance: {self.balance}"

    # ===============================
    # 2️⃣ Class Method
    # ===============================
    @classmethod
    def get_total_accounts(cls):
        """
        Class method:
        - Works with class data (cls)
        - Cannot access instance variables directly
        """
        return f"Total accounts in {cls.bank_name}: {cls.total_accounts}"

    # ===============================
    # 3️⃣ Static Method
    # ===============================
    @staticmethod
    def is_valid_amount(amount):
        """
        Static method:
        - Independent method
        - Does NOT use self or cls
        - Just utility/helper logic
        """
        return amount > 0


# ===============================
# 🔹 Using the class
# ===============================

# Creating objects
acc1 = BankAccount("Tasin", 1000)
acc2 = BankAccount("Rahim", 500)

# ✅ Instance method (called using object)
print(acc1.deposit(200))  
# Output: Tasin new balance: 1200

# ✅ Class method (called using class)
print(BankAccount.get_total_accounts())  
# Output: Total accounts in ABC Bank: 2

# ✅ Static method (utility check)
print(BankAccount.is_valid_amount(100))  
# Output: True


#| Type            | Uses                   | Access              |
#| --------------- | ---------------------- | ------------------- |
#| Instance Method | Works with object data | `self`              |
#| Class Method    | Works with class data  | `cls`               |
#| Static Method   | Just helper function   | No `self`, no `cls` |





#=======================================================================================================================================================================================
'''
✅ 1. Instance Methods
✔️ When to use:
    You want to access or modify data specific to an instance of the class.
    These always take self as the first argument.
'''

#instance method (using self)
class MathUtils:
    def add(self, a, b):
        return a + b
        
#object/instance needed
obj = MathUtils()
result = obj.add(3, 5)
print(result)

'''
⚠️ Key Differences:

Decorator	            First Arg	                Accesses self or cls?	            Purpose

@staticmethod	        None	                    ❌ No	                            General utility logic
@classmethod	        cls	                        ✅ Class-level access	            Factory methods, alternative constructors
Instance method	        self	                    ✅ Instance-level access	        Regular object behavior
'''
#========================================================================================================================================================
'''
                                                        classmethod and staticmethod
                                                    Static method(explained at the bottom)
'''
'''
When it's a general information about the whole project or code, then we should use @staticmethod
No need to use self (as a argument) on the @staticmethod, because in staticmethod, we don't use any instance here 

or I can also say formally :
-When it's a general-purpose utility or logic that doesn’t depend on instance (self) or class (cls) variables or methods, use @staticmethod.
-For general utility functions that don't depend on object state (e.g., calculations, data validation, etc.).
'''
class Geeks:
    course = 'DSA'
    list_of_instances = []

    def __init__(self, name):
        self.name = name
        Geeks.list_of_instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course: {cls.course}"

    @classmethod
    def get_instance_count(cls):
        return f"Number of instances: {len(cls.list_of_instances)}"

    @staticmethod
    def welcome_message():
        return "Welcome to Geeks for Geeks!"

# Creating instances
g1 = Geeks('Alice')
g2 = Geeks('Bob')

# Calling class methods
print(Geeks.get_course())  
print(Geeks.get_instance_count())  

# Calling static method
print(Geeks.welcome_message())



#========================================================================================================================================================

# Example 
#Approach -1 (using instance method)
class Employee:
    incriment=0.02 #incriment is a class variable 
    def __init__(self,f,l=None,sal=None):#default arguments,must be filling from right to left .
    # if I miss passing some argument, by default these variables will take None.
    # we can put here some ohter arguments value 

        self.first=f
        self.last=l
        self.salary=sal
        self.fullname=self.first+' '+self.last
    
    def set_incri_salary(self):#it's a instance method
        self.salary+=self.salary*Employee.incriment
    
    def get_emp_details(self):#it's a method
        print('Name: ',self.fullname)
        print('Salary: ',self.salary)

emp1=Employee('Samuel','Edison',10000)
emp2=Employee('Tomas','Alva',20000)
emp1.get_emp_details()
emp2.get_emp_details()
emp1.set_incri_salary()
emp2.set_incri_salary()
emp1.get_emp_details()
emp2.get_emp_details()



#========================================================================================================================================================

#Approach : 2 - using class method

'''
it's always better to use @classmethod to change or update the class variable,instead of using instance method(explained here below-" Common Mistake to Avoid"),
if u want to update instance variable = use instance method
if u want to update class variable = use classmethod

so we can say
🚨 Use @classmethod to access or modify class variables.
🚨 Use instance methods (with self) to access or modify instance variables.

📌 Why?
✅ Class Method (cls)

    🔹 Operates on the class itself, not a specific object.
    🔹 Can access and modify class variables (shared across all instances).
    
✅ Instance Method (self)

   🔹Operates on a specific object instance.
   🔹Can access and modify instance variables (unique per object).
'''

class Employee:
    incriment=0.02 #✔️class variable 
    def __init__(self,f,l=None,sal=None):

        self.first=f
        self.last=l
        self.salary=sal
        self.fullname=self.first+' '+self.last
    
    def set_incri_salary(self):#it's a instance method
        self.salary+=self.salary*Employee.incriment
    
    def get_emp_details(self):#it's a instance method
        print('Name: ',self.fullname)
        print('Salary: ',self.salary)
    
    @classmethod
    def set_incri_percentage(self,new_percentage):
        self.incriment=new_percentage


emp1=Employee('Samuel','Edison',10000)
emp2=Employee('Tomas','Alva',20000)
Employee.set_incri_percentage(0.07)#using class name to call the class method,
                                   #can also use emp1 or emp2 object to call the class method
emp1.set_incri_salary()
emp2.set_incri_salary()
emp1.get_emp_details()
emp2.get_emp_details()


'''
✅ cls is just a naming convention, not a keyword like def or return.
🟡 You can use any name, but should use cls to follow Python best practices and make your code understandable to others (and your future self!).
'''

'''
❌ Common Mistake to Avoid
Using an instance method to update a class variable only affects that one instance, unless you reference the class explicitly:
'''

class Test:
    value = 0

    def wrong_update(self):
        self.value += 1  # ❌ Creates instance variable, doesn't change class value

'''Now self.value becomes an instance variable, hiding the class variable.'''

#========================================================================================================================================================

#STEP:3 Use @classmethod to create an alternative constructor

#if we don't use classmethod 
class Employee:
    def __init__(self,f,l=None,add=None):#it's a instance method

        self.first=f
        self.last=l
        self.fullname=self.first+' '+self.last
        self.address=add
    
    def get_emp_details(self):#it's a instance method
        print('Name: ',self.fullname)
        print('Address: ',self.address)


emp1=Employee('Samuel','jhon','india')
emp1.get_emp_details()

emp1_info='Sam,Carun,England'
first,second,address=emp1_info.split(',')
'''
Giving the info about the person in a comma separeted string ,& then spreading it with 
the help of split method.Then storing into three different variables 
'''
emp2=Employee(first,second,address)#crating an instance(Employee) and passing these 3 variables
emp2.get_emp_details()




#=========now,if we use the classmethod to create the alternative constructor ==================

class Employee:
    def __init__(self,f,l=None,add=None):
        self.first=f
        self.last=l
        self.fullname=self.first+' '+self.last
        #or we can do -
        #self.fullname = f"{self.first} {self.last}"  # Using f-string
        self.address=add
    
    def get_emp_details(self):#it's a instance method
        print('Name: ',self.fullname)
        print('Address: ',self.address)
    @classmethod
    def update_new_info(cls,info):
       first,second,address=emp1_info.split(',')#spliting the string and storing it into 3 different variables 
       return self(first,second,address)# Return new Employee instance

emp1=Employee('Samuel','jhon','india')
emp1.get_emp_details()

emp1_info='Sam,Ali,Canada'

emp2=Employee.update_new_info(emp1_info)#calling the class method using class name (by creating instance of Employee class)
emp2.get_emp_details()

'''
✔️✔️✔️What is an alternative constructor?

    A normal constructor in Python is __init__, which is used like this:

user = User("Tasin", 25)

An alternative constructor is a special class method that creates an object in a different way than the regular __init__ method like from a string, dictionary, or file.
It’s like having multiple doors to enter the same room.
    
✔️Why Is update_new_info is an Alternative Constructor?

    It provides a different way to create an Employee:

        By Normal constructor: Employee('Sam', 'Ali', 'Canada')

        By Alternative constructor: Employee.update_new_info('Sam,Ali,Canada')

    Useful when input comes in a non-standard format (e.g., CSV strings, JSON).


✔️Key points about alternative constructors:

Purpose: They provide different ways to create instances of a class
Common pattern: Use @classmethod decorator and cls as the first parameter
Return value: Always return cls(...) to create a new instance
Use cases: When you need to create objects from different data formats (like strings, dictionaries, files, etc.)
'''

#========================================================================================================================================================


#STATIC METHOD

'''
No implicit arguments:
Unlike instance methods (which take self as the first argument) or class methods (which take cls), static methods do not receive any implicit first argument.

Here we'll use staticmethod to print information,
staticmethod associated with the class and can be called directly on the class itself without creating an instance.

Cannot modify class or instance state:
Static methods do not have access to instance-specific attributes or class-specific attributes


When to use static methods:

    When a function is logically related to a class but does not need to access any specific instance or class data.
    For utility functions or helper methods that are relevant to the class but are independent of the object's state.
    To group related functions within a class for better code organization.

    if we want to something inside class but it's not related to anything to do with the class 
    information means no process is going to happen because of that,
    then we should use static method 

When it's a general information about the whole project or code, then we should use @staticmethod
No need to use self (as a argument) on the @staticmethod, because in staticmethod, we don't use any instance here 
'''

#Example 1:
class Validator:
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

# Usage
print(Validator.is_valid_email("hello@example.com"))  # True
print(Validator.is_valid_email("helloexamplecom"))    # False


# Example 1:
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Usage (no instance/object needed!)
result = MathUtils.add(3, 5)  # Output: 8

'''
✅ Benefits:
    No need to create an object — saves memory, cleaner code.
    Makes it clear: this method doesn't use or need instance data (self) or class data (cls).
    Ideal for utility/helper functions.
'''


# if we dont use static method - instance method (using self)
class MathUtils:
    def add(self, a, b):
        return a + b
#object needed

obj = MathUtils()
result = obj.add(3, 5)
print(result)


# Example 2

class Employee:
    cnt_employee=0
    def __init__(self,f,l=None,add=None):
        Employee.cnt_employee+=1 # or  self.__class__.cnt_employee += 1
        self.first=f
        self.last=l
        self.fullname=self.first+' '+self.last
        self.address=add
    
    def get_emp_details(self):#it's a instance method
        print('Name: ',self.fullname)
        print('Address: ',self.address)
    @staticmethod
    def number_of_employee():
        print(f'Total number of employee:{Employee.cnt_employee},so total {Employee.cnt_employee} objects cereated ')


emp1=Employee('Samuel','jhon','india')
emp2=Employee('Sam','Ali','Canada')

# Accessing instance methods and static method
emp1.get_emp_details()
emp2.get_emp_details()
# Accessing static method
Employee.number_of_employee()

#=================================================================================================================================================================================================\
