'''
The below code shows how Python can use two different class types, in the same way.
We create a for loop that iterates through a tuple of objects. 
Then call the methods without being concerned about which class type each object is.
We assume that these methods actually exist in each class. 
'''
'''
Runtime Polymorphism: Occurs when the behavior of a method is determined at runtime based on the type of the object.
'''

class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):  
  '''Runtime Polymorphism'''
  country.capital()
  country.language()
  country.type()

'''
Output

New Delhi is the capital of India.
Hindi is the most widely spoken language of India.
India is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.

'''
#==============================================================================================================================================================================
#Ex-2
class Student(object):
    def name(self):
        print("Student name is Tasin")
    def age(self):
        print("Student age 24")
    def weight(self):
        print("Student weight is 67")
    
class Teacher(object):
    def name(self):
        print("Teacher name is Abdur Rahim")
    def age(self):
        print("Teacher age 50")
    def weight(self):
        print("Teacher weight 80")



obj=Student()
obj2=Teacher()

for i in (obj,obj2):  
  '''Runtime Polymorphism'''
  i.name()
  i.age()
  i.weight()

#=======================================================================================================================================================================

# Another Example : 

class Bank1:
    def __init__(self, name, rt, limit, number):
        self.name = name
        self.rt = rt
        self.limit = limit
        self.number = number

    def show_name(self):
        print("Name:", self.name)

    def interest_rate(self):
        print("Interest Rate:", self.rt)

    def loan_limit(self):
        print("Loan Limit:", self.limit)

    def employee_size(self):
        print("Employee Size:", self.number)


class Bank2:
    def __init__(self, name, rt, limit, number):
        self.name = name
        self.rt = rt
        self.limit = limit
        self.number = number

    def show_name(self):
        print("Name:", self.name)

    def interest_rate(self):
        print("Interest Rate:", self.rt)

    def loan_limit(self):
        print("Loan Limit:", self.limit)

    def employee_size(self):
        print("Employee Size:", self.number)


# Polymorphism in action
bn1 = Bank1("Dhaka Bank", 2.5, 40000, 500)
bn2 = Bank2("Asia Bank", 3.5, 20000, 700)

for bank in (bn1, bn2):  # Runtime polymorphism
    bank.show_name()
    bank.interest_rate()
    bank.loan_limit()
    bank.employee_size()
    print("-----")



# Output:

# Name: Dhaka Bank
# Interest Rate: 2.5
# Loan Limit: 40000
# Employee Size: 500
# -----
# Name: Asia Bank
# Interest Rate: 3.5
# Loan Limit: 20000
# Employee Size: 700
# -----







    
